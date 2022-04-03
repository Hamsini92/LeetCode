class solution:
    def angle_between_hour(self,hour: int, minutes: int):

        one_minute_angle = 6
        one_hour_angle = 30

        minute_angle = minutes * one_minute_angle
        hour_angle = (hour % 12 + minutes/60) * one_hour_angle

        angle_diff = abs(hour_angle - minute_angle)

        return min(angle_diff, 360-angle_diff)

