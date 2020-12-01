class TimeToolsUtils:
    """
    A helper class to the TimeTools class.

    It has some methods used on TimeTools class that
    need to exist but wouldn't be nice if maintained 
    on the class itself.
    """

    def __format_result(self, result: str) -> str:
        """
        Used to format the result returned
        on the convert_seconds method from TimeTools class.

        -- Parameters:
            result(str): the result to be formatted

        -- Return:
            str: the new result formatted according to the format '00:00:00'

        """
        hours, minutes, seconds = result.split(':')

        if len(hours) == 1:
            hours = f'0{hours}'

        if len(minutes) == 1:
            minutes = f'0{minutes}'

        if len(seconds) == 1:
            seconds = f'0{seconds}'

        res = f'{hours}:{minutes}:{seconds}'

        return res

class TimeTools(TimeToolsUtils):
    def calculate_seconds(self, time: str) -> int:
        hours, minutes, seconds = time.split(':')

        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        return (hours * 60 * 60) + (minutes  * 60) + seconds

    def convert_seconds(self, seconds: int) -> str:
        final_seconds = 0
        final_minutes = 0
        final_hours = 0

        if seconds % 60 == 0:
            final_minutes = seconds / 60

            if final_minutes >= 60:
                final_hours = int(final_minutes / 60)
                final_minutes = 0

        else:
            int_minutes_part = int(str(seconds / 60).split('.')[0])

            final_minutes = int_minutes_part
            final_seconds = seconds % 60

            if final_minutes >= 60:
                int_hours_part = int(str(final_minutes / 60).split('.')[0])

                final_hours = int_hours_part
                final_minutes = final_minutes % 60

        res = f'{final_hours}:{final_minutes}:{final_seconds}'
        
        return self.__format_result(res)
