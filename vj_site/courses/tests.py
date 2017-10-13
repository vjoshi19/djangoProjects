from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course
from .models import Step

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write Regular Expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python DataStructures",
            description="Learn about different DS python has to offer"
            )

    def test_step_creation(self):
        step = Step.objects.create(
            title="Lists - TestTitle",
            description="Learn to create lists in python",
            content="array and lists mean the same",
            course=self.course
            )

        self.assertIn(step, self.course.step_set.all())

class CourseViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in python"
        )
        self.course2 = Course.objects.create(
            title="New Course",
            description="A New Course"
        )
        self.step=Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in docstrings.",
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={
            'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertContains(resp, self.course.description)

    def test_step_detail(self):
        resp = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.step.pk
            }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])

