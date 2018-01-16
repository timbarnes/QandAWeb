from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from registration.views import RegistrationView

from educate.models import Subject, Category, Article
from users.models import Profile, Favorites, Note, Task, TaskList
from users.forms import ProfileForm, UserDataForm, TaskListForm,
    NoteForm, TaskForm, RegistrationForm


class UserRegistrationView(RegistrationView):
    """Customized registration includes creation of the empty profile.
    """
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    disallowed_url = reverse_lazy('home')

    def register(self, request, **cleaned_data):
        """Custom registration view.
        """
        print('Starting registration')
        print(cleaned_data)
        u = User.objects.create_user(
            cleaned_data['username'],
            '',
            cleaned_data['password1'])
        p = Profile()
        p.user = u
        p.save()
        messages.success(self.request,
                         'Thank you for registering. Now you can login.')


class ProfileView(generic.TemplateView):
    """View/edit profile data
    """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy('userdataUpdate',
                                                    args=[self.request.user.pk])
        profile_form.helper.form_action =
            reverse_lazy('profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(Profile,
                                         user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        return context


class UpdateProfileView(generic.edit.UpdateView):
    """Save updated profile data. Called only with POST.
    """
    model = Profile
    fields = ['picture', 'home', 'interests', 'objectives']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action =
        reverse_lazy('userdataUpdate', args=[self.request.user.pk])
        profile_form.helper.form_action =
        reverse_lazy('profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(Profile, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        return context

    def form_valid(self, form):
        self.kwargs['form_data'] = form.cleaned_data
        messages.success(self.request, 'Profile successfully updated')
        return super(UpdateProfileView, self).form_valid(form)


class UpdateUserDataView(generic.edit.UpdateView):
    """Save updated user data. Called only with POST.
    """
    model = User
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserDataView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy('userdataUpdate',
                                                    args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate',
                                                       args=[profile.pk])
        context.update({
            'profile':
            get_object_or_404(Profile,
                              user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        print('UpdateUserDataView: ', context)
        return context

    def form_invalid(self, form):
        print("form invalid", form)
        messages.error(self.request, 'User data not successfully updated.')
        return super(UpdateUserDataView, self).form_invalid(form)

    def form_valid(self, form):
        print("Form submitted: ", form)
        self.kwargs['form_data'] = form.cleaned_data
        messages.success(self.request, 'User data successfully updated')
        return super(UpdateUserDataView, self).form_valid(form)


class MyHomeView(generic.TemplateView):
    """Home page for each user.
    """
    template_name = 'users/myhome.html'

    def get_context_data(self, **kwargs):
        print('MYHOME')
        context = super(MyHomeView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, user=self.request.user),
            'favorites': Favorites.objects.filter(user=self.request.user),
            'tasklists': TaskList.objects.filter(user=self.request.user),
            'notes': Note.objects.filter(user=self.request.user),
            'subject_subset': Subject.objects.filter(author=self.request.user),
            'category_subset': Category.objects.filter(author=self.request.user),
            'article_subset': Article.objects.filter(author=self.request.user),
        })
        print(context)
        return context


class NotesView(generic.FormView):
    """Home page for each user.
    """
    template_name = 'users/notes.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')

    def get_context_data(self, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        context.update({
            'notes': Note.objects.filter(user=self.request.user),
        })
        return context

    def form_valid(self, form):
        print("Form submitted: ", form)
        self.kwargs['form_data'] = form.cleaned_data
        n = form.save(commit=False)
        n.user = self.request.user
        n.slug = slugify(form.cleaned_data['title'])
        n.save()
        form.save_m2m()
        messages.success(self.request, 'Note saved')
        return super(NotesView, self).form_valid(form)


class TaskListsView(generic.FormView):
    """Display task lists.
    """
    template_name = 'users/tasklists.html'
    form_class = TaskListForm
    success_url = reverse_lazy('taskLists')

    def get_context_data(self, **kwargs):
        context = super(TaskListsView, self).get_context_data(**kwargs)
        context.update({
            'task_lists': TaskList.objects.filter(user=self.request.user),
        })
        return context

    def form_valid(self, form):
        print("Form submitted: ", form)
        self.kwargs['form_data'] = form.cleaned_data
        t = form.save(commit=False)
        t.user = self.request.user
        t.slug = slugify(form.cleaned_data['name'])
        t.save()
        form.save_m2m()
        messages.success(self.request, 'Task list created')
        return super(TaskListsView, self).form_valid(form)


class TasksView(generic.TemplateView):
    """Display tasks associated with a tasklist.
    """
    template_name = 'users/tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        context.update({
            'taskslists': TaskList.objects.filter(user=self.request.user),
            'tasklist': get_object_or_404(TaskList, slug=self.kwargs['slug']),
            'tasks': Task.objects.filter(tasklist__slug=self.kwargs['slug']).order_by('done'),
            'tasklists': TaskList.objects.filter(user=self.request.user),
        })
        return context


class NewNoteView(generic.FormView):
    """Add a note.
    """
    template_name = 'users/newnote.html'
    form_class = NoteForm

    def get_context_data(self, **kwargs):
        context = super(NewNoteView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
            'form': NoteForm(user=self.request.user),
        })
        return context


class NewTaskView(generic.FormView):
    """Add a task to an existing tasklist.
    """
    template_name = 'users/newtask.html'
    form_class = TaskForm
    success_url = reverse_lazy('taskLists')

    def get_context_data(self, **kwargs):
        context = super(NewTaskView, self).get_context_data(**kwargs)
        tlist = get_object_or_404(TaskList, slug=self.kwargs['slug'])
        context.update({
            'tasklist': tlist,
            'tasks': Task.objects.filter(tasklist=tlist.id),
            'form': TaskForm({'tasklist': tlist.pk, }),
            'tasklists': TaskList.objects.filter(user=self.request.user),
        })
        return context

    def form_valid(self, form):
        print('Due =', form.cleaned_data['due'], '=')
        if not form.cleaned_data['due']:
            form.cleaned_data['due'] = None
            print(form)
        print(form)
        t = form.save()
        t.slug = slugify(form.cleaned_data['task'])
        t.save()
        messages.success(self.request, 'Task created.')
        return super(NewTaskView, self).form_valid(form)


class NoteView(generic.UpdateView):
    """Alter an existing user note.
    """
    template_name = 'users/note.html'
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('notes')


class TaskView(generic.UpdateView):
    """Alter an existing user task.
    """
    template_name = 'users/task.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('tasks', args=[self.object.tasklist.slug])
