class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingPixel = image[sr][sc]

        if startingPixel == color:
            return image

        self.dfs(image, sr, sc, color, startingPixel)
        return image

    def dfs(self, image, sr, sc, color, startingPixel):
        if (sr < 0 or sr >= len(image) or
            sc < 0 or sc >= len(image[0]) or
            image[sr][sc] != startingPixel):
            return

        image[sr][sc] = color

        self.dfs(image, sr + 1, sc, color, startingPixel)
        self.dfs(image, sr - 1, sc, color, startingPixel)
        self.dfs(image, sr, sc + 1, color, startingPixel)
        self.dfs(image, sr, sc - 1, color, startingPixel)