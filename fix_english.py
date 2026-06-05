f = open('index.html').read()

replacements = [
    # Hero proof text
    ("Market traders don dey use Pigo — <strong>join dem today</strong>",
     "Market traders are already using Pigo — <strong>join them today</strong>"),

    # Pidgin hook lines
    ('<div class="pidgin-line">How far!</div>',
     '<div class="pidgin-line">Hello!</div>'),

    ('Your money dey count?',
     'Is your money being tracked?'),

    # Step 1
    ("Pigo sets you up in 60 seconds — in Pidgin.",
     "Pigo sets you up in 60 seconds — in English or Pidgin."),

    # Step 2
    ("Pigo understands plain Pidgin and English — just describe what happened.",
     "Pigo understands plain English and Pidgin — just describe what happened."),

    # Step 3
    ("You just sell — Pigo counts every kobo.",
     "You just sell — Pigo counts every naira."),

    # FAQ
    ("Wetin happen if my credits finish?",
     "What happens when my credits run out?"),

    ("My business get multiple people — can dem all use Pigo?",
     "My business has multiple people — can they all use Pigo?"),

    # Final CTA
    ("tracking every kobo. Free to start. No download. No wahala.",
     "tracking every naira. Free to start. No download. No hassle."),

    # og:description
    ("Every kobo — counted.",
     "Every naira — counted."),
]

count = 0
for old, new in replacements:
    if old in f:
        f = f.replace(old, new)
        count += 1
        print(f'fixed: {old[:50]}...')
    else:
        print(f'SKIP: {old[:50]}...')

open('index.html', 'w').write(f)
print(f'\ndone: {count} replacements')
