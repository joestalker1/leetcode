class Solution:
    def minHeightShelves(self, books, shelf_width) :
        if not books:
            return 0

        def place_book(i, cur_width, max_book_height, height_so_far):
            if i == len(books):
                if cur_width <= shelf_width:
                    return height_so_far + max_book_height
                return float('inf')
            if cur_width > shelf_width:
                return float('inf')

            # place i book at current shelf
            total_height1 = place_book(i + 1, cur_width + books[i][0], max(books[i][1], max_book_height), height_so_far)
            # place i book at the next shelf
            total_height2 = place_book(i + 1, books[i][0], books[i][1], height_so_far + max_book_height)
            return min(total_height1, total_height2)

        return place_book(0, 0, 0, 0)


sol = Solution()

print(sol.minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10))#15
#print(sol.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))




