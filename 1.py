class Solution:
    def solve(self,ind: int, s: int, l: List[int], arr: List[int], ans: List[List[int]]):
        n=len(arr)
        if ind==n:
            if s==0:
                ans.append(l.copy())
            return 
        if arr[ind]<=s:
            l.append(arr[ind])
            self.solve(ind,s-arr[ind],l,arr,ans)
            l.pop()
        self.solve(ind+1,s,l,arr,ans)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.solve(0,target,[],candidates,ans)
        return ans

