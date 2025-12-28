from swagger_coverage_tool import SwaggerCoverageTracker


tracker_auth = SwaggerCoverageTracker(service="auth-api")
tracker_booking = SwaggerCoverageTracker(service="booking-api")
tracker_room = SwaggerCoverageTracker(service="room-api")
tracker_report = SwaggerCoverageTracker(service="auth-api")
tracker_branding = SwaggerCoverageTracker(service="branding-api")
tracker_message = SwaggerCoverageTracker(service="message-api")