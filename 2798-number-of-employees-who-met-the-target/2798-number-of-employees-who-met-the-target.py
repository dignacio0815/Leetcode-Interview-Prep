class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        return self.solutionUsingForLoop(hours, target)
        
        
    def solutionUsingForLoop(self, hours: List[int], target: int) -> int:
        employeeCount = 0
        
        for h in hours:
            if h >= target:
                employeeCount += 1
                
        return employeeCount