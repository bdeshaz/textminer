import re

text = """Dear Mr. Davis,

I got to know of your company through our mutual friend Fiona Williams and the
training you offer to graduate students in Advertising.

I am a graduate student of Mass Communications with specialization in
Advertising.  I am currently pursuing the last year of my course.
I would very much like to see firsthand the work environment in an advertising
agency.

If you would like a reference, my advisor can be reached at (454) 999-1212.

You can contact me at (919) 123-4569 at your convenience."""



def phone_numbers(text):
    phone_book = re.findall(r"\(?(\d{3})\)?[\.\-]?\s*(\d{3})[\.\-]?(\d{4})", text)
    return phone_book

print(phone_numbers(text))
