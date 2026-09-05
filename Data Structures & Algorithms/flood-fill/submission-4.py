class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        
        if start == color:
            return image
        
      

        self.dfs(image, sr, sc, color, start)

        return image

    def dfs(self, image, sr, sc, color, start):

        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != start):
            return 


        image[sr][sc] = color

        self.dfs( image, sr + 1, sc, color, start)
        self.dfs( image, sr - 1, sc, color, start)
        self.dfs( image, sr, sc + 1, color, start)
        self.dfs( image, sr, sc - 1, color, start)

        
        #The length of a column is the number of rows assuming they are all filled - len(image)
        #The length of a row is the length of an image index - len(image[0])
        