class Rulebook():
    def __init__(self) -> None:
        self.reverse_lookup:dict[int,list[int]] = {}

    def add_rule(self, rule_str:str) -> None:
        '''
        Adds a rule from the input to the rulebook.
        A rule is in the format "X|Y"
        '''
        left,right = [int(_) for _ in rule_str.split('|')]
        # Add the reverse lookup
        if right in self.reverse_lookup:
            self.reverse_lookup[right].append(left)
        else:
            self.reverse_lookup[right] = [left]
    
    def validate(self, update_line:str) -> bool:
        '''
        Validate an update.
        For each page in the list:
            - Look at the all the pages seen so far
            - Check the reverse rules for our current page
            - If any pages in that list show up in all_pages and NOT in our seen list then invalidate
        '''
        pages:list[int] = [int(_) for _ in update_line.split(',')]
        all_pages:set[int] = set(pages)
        seen_pages:set[int] = set()
        for page in pages:
            seen_pages.add(page)
            prev_pages:list[int] = self.reverse_lookup.get(page, [])
            for prev_page in prev_pages:
                if prev_page in all_pages and prev_page not in seen_pages:
                    # this means the page should come before this one but it doesn't.
                    return False
        return True

    def fix_update(self, update_line:str)->list[int]:
        '''
        Fix an invalid update line, and return the resulting correct line.
        For this one, I'm thinking we check the line until we hit an bad order, 
        and swap those two pages then run it again. Kinda like bubble sort.
        '''
        pages:list[int] = [int(_) for _ in update_line.split(',')]
        all_pages:set[int] = set(pages)
        while (to_swap := self.find_bad_rule(pages)) != None:
            pages = self.swap(pages,to_swap)
        return pages
    
    def find_bad_rule(self, pages:list[int]) -> tuple[int, int] | None:
        '''
        Returns the indexes of the two bad rules to swap, or None if it's valid.
        '''
        seen_pages:set[int] = set()
        for page in pages:
            seen_pages.add(page)
            prev_pages:list[int] = self.reverse_lookup.get(page, [])
            for prev_page in prev_pages:
                if prev_page in pages and prev_page not in seen_pages:
                    # this means the page should come before this one but it doesn't.
                    return (pages.index(page),pages.index(prev_page))
        return None

    def swap(self,pages:list[int],to_swap:tuple[int, int]) -> list[int]:
        '''
        Swaps the values at the two indexes given
        '''
        tmp:int = pages[to_swap[0]]
        pages[to_swap[0]] = pages[to_swap[1]]
        pages[to_swap[1]] = tmp
        return pages