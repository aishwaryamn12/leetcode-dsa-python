def fullJustify(words, maxWidth):
    res = []
    i = 0

    while i < len(words):
        # Find how many words fit in the line
        line_len = len(words[i])
        j = i + 1

        while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
            line_len += len(words[j])
            j += 1

        line_words = words[i:j]
        num_words = j - i
        spaces_needed = maxWidth - line_len

        # Case 1: Last line OR single word → left justified
        if j == len(words) or num_words == 1:
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        else:
            # Case 2: Fully justified
            gaps = num_words - 1
            space_per_gap = spaces_needed // gaps
            extra_spaces = spaces_needed % gaps

            line = ""
            for k in range(gaps):
                line += line_words[k]
                line += " " * (space_per_gap + (1 if k < extra_spaces else 0))
            line += line_words[-1]

        res.append(line)
        i = j

    return res
