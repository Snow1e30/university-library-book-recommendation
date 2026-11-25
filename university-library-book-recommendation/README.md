# University Library Book Recommendation System

A Python-based, deterministic and rule-based recommendation system that helps university students find relevant library books using their academic requirements.

The project is designed around the supplied university assignment specification and demonstrates Python concepts from Modules 1–3.

## Features

- Student input and validation: programme, semester, subject, topic, difficulty level and reading purpose.
- Library catalogue containing 30 sample books.
- Catalogue represented as a list of dictionaries; topics and programmes use tuples.
- Search by subject, author, topic, programme or book type.
- Subject-wise and topic-wise searches.
- Rule-based recommendation scoring and descending ranking.
- Explanation of every recommendation.
- Five recommendation categories.
- Top-N recommendations using list slicing.
- Option to show all relevant books or only available books.
- Recommendation summary with execution date and time.
- Automated unit tests using Python's built-in `unittest` module.

## Recommendation scoring

| Criterion | Points |
|---|---:|
| Exact subject match | +5 |
| Requested topic is covered | +4 |
| Programme match | +2 |
| Difficulty level match | +3 |
| Reading purpose/book type match | +2 |
| Book is currently available | +1 |
| **Maximum** | **17** |

### Recommendation categories

| Score | Category |
|---:|---|
| 14–17 | Highly Recommended |
| 10–13 | Recommended |
| 6–9 | Moderately Relevant |
| 1–5 | Low Relevance |
| 0 | Not Relevant |

### Purpose matching

The application accepts these reading purposes and maps them to catalogue book types:

- Study → Textbook or Supplementary
- Reference → Reference
- Research → Research or Reference
- Supplementary learning → Supplementary or Textbook

A direct purpose/book-type match is also accepted.

**Semester note:** Semester is collected and displayed as part of the student's academic requirements. The supplied scoring framework does not award semester-match points, so semester does not change the maximum score of 17.

## Requirements

- Python 3.8 or later
- No external packages
- No database
- No internet connection required to run the program

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Run tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
university-library-book-recommendation/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── tests/
│   └── test_main.py
└── screenshots/
    └── README.txt
```

## Main functions

| Function | Purpose |
|---|---|
| `display_library()` | Displays the complete catalogue |
| `search_books()` | Searches by subject, author, topic, programme or book type |
| `calculate_score(book, student_requirements)` | Calculates a score out of 17 |
| `recommend_books(student_requirements)` | Evaluates and ranks the catalogue |
| `recommendation_category(score)` | Assigns a recommendation category |
| `explain_recommendation(book, student_requirements)` | Produces the reasons behind a score |
| `subject_wise_recommendations()` | Finds books for a subject |
| `topic_wise_search()` | Finds books covering a topic |
| `print_summary(all_results, relevant_results)` | Displays recommendation statistics |

## Python concepts demonstrated

- Variables, input and output
- Operators and conditional statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Lists, tuples and dictionaries
- String methods (`strip`, `casefold`)
- Functions, arguments and return values
- Lambda functions for sorting
- List slicing for Top-N results
- `datetime` module for execution timestamp
- List comprehensions

