class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(' ')
        
        date[0] = "".join([char for char in date[0] if char in '0123456789'])
        if len(date[0]) == 1:
            date[0] = '0' + date[0]
        
        month = {
            "Jan": '01',
            "Feb": '02',
            "Mar": '03',
            "Apr": '04',
            "May": '05',
            "Jun": '06',
            "Jul": '07',
            "Aug": '08',
            "Sep": '09',
            "Oct": '10',
            "Nov": '11',
            "Dec": '12'
        }
        
        return date[2] + "-" + month[date[1]] + "-" + date[0]
        
