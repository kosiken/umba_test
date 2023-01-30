import math


# This is a helper class to create and render pagination blocks
class PageItem:
    def __init__(self, page: int, value: str):
        self.page = page
        self.value = value

    def __str__(self):
        return str(self.page)

    # This method is used to create pagination tiles in the html rendered
    # later on
    @staticmethod
    def create_page_items(page: int, num_pages: int):
        arr = [PageItem(i, str(i)) for i in range(1, num_pages) if i < num_pages + 1]
        prev5 = (math.floor(page / 5) * 5)

        if len(arr) > 7:
            if prev5 < 5:
                arr = arr[0:1] + arr[1:4]
            elif prev5 < num_pages:
                prev5 = prev5 - 1
                arr = arr[0:1] + [PageItem(-1, '...')] + arr[prev5:prev5 + 5]
            if arr[len(arr) - 1]:
                arr.append(PageItem(num_pages, str(num_pages)))
            else:
                arr.append(PageItem(-1, '...'))
                arr.append(PageItem(num_pages, str(num_pages)))
        return arr
