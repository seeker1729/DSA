'''
Approach:
-> Sort the jobs in descending order of profit (we want to ensure that we do the jobs which give us more
profit)
->To decide when it should be done => do it as late as possible so you can do other jobs early on to improve the
profit
TC : O(nlogn) SC : O(n) 
'''


class Solution:
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda x : x.profit, reverse = True)
        maxDeadline = 0
        for job in Jobs:
            maxDeadline = max(maxDeadline, job.deadline)
        profit = 0
        jobsPerformed = [-1] * (maxDeadline + 1)
        countJobs = 0
        for job in Jobs:
            curDeadline = job.deadline
            for i in range(curDeadline, 0, -1):
                if jobsPerformed[i] == -1:
                    jobsPerformed[i] = job.id
                    countJobs += 1
                    profit += job.profit
                    break
        return (countJobs, profit)

