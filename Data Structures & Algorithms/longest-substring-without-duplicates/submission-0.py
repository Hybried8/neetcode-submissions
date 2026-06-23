class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = [] # Initialize your tracking list
        maxcount = 0 # Maxcount variable

        for i in s:
            if i not in track:
                track.append(i)
                # Using max() is a slightly cleaner way to do your if len(track) > maxcount check
                maxcount = max(maxcount, len(track))
            else:  # 'i in track' (We encountered a duplicate!)
                # 1. Find where the duplicate is in our history
                duplicate_index = track.index(i)
                
                # 2. Slice the list to keep ONLY what's AFTER the duplicate
                track = track[duplicate_index + 1:]
                
                # 3. Append the new character
                track.append(i)
        
        return maxcount