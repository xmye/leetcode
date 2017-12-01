class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        countU = countD = countL =countR = j = 0
        while j < len(moves):   
            if moves[j] == 'U':
                countU += 1
            if moves[j] == 'D':
                countD += 1
            if moves[j] == 'L':
                countL += 1
            if moves[j] == 'R':
                countR += 1
            j += 1
        if(countU == countD and countL == countR):
            return True
        return False