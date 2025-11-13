from rest_framework.routers import DefaultRouter
from .api_views import CourseViewSet, InstructorViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"instructors", InstructorViewSet)
router.register(r"enrollments", EnrollmentViewSet)

urlpatterns = router.urls
