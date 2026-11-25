"""
University Library Book Recommendation System
A deterministic, rule-based Python project for university students.

Run:
    python main.py

No third-party packages or database are required.
"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Library catalogue
# The catalogue is a list of dictionaries; topics are stored as tuples.
# ---------------------------------------------------------------------------

LIBRARY: List[Dict] = [
    {
        "book_id": "B001", "title": "Advanced Accountancy", "author": "R. L. Gupta",
        "subject": "Advanced Corporate Accounting",
        "topics": ("Consolidation of Accounts", "Amalgamation", "Internal Reconstruction"),
        "programmes": ("B.Com", "M.Com"), "level": "Intermediate",
        "book_type": "Reference", "year": 2022, "available": True,
    },
    {
        "book_id": "B002", "title": "Corporate Accounting", "author": "S. P. Jain",
        "subject": "Advanced Corporate Accounting",
        "topics": ("Consolidation of Accounts", "Issue of Shares", "Company Final Accounts"),
        "programmes": ("B.Com", "M.Com"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2021, "available": True,
    },
    {
        "book_id": "B003", "title": "Financial Reporting", "author": "S. N. Maheshwari",
        "subject": "Financial Accounting",
        "topics": ("Financial Statements", "Cash Flow Statement", "Accounting Standards"),
        "programmes": ("B.Com", "BBA", "M.Com"), "level": "Advanced",
        "book_type": "Reference", "year": 2023, "available": False,
    },
    {
        "book_id": "B004", "title": "Management Accounting", "author": "Khan and Jain",
        "subject": "Management Accounting",
        "topics": ("Ratio Analysis", "Budgetary Control", "Marginal Costing"),
        "programmes": ("B.Com", "BBA", "M.Com"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2020, "available": True,
    },
    {
        "book_id": "B005", "title": "Cost Accounting", "author": "M. N. Arora",
        "subject": "Cost Accounting",
        "topics": ("Marginal Costing", "Process Costing", "Standard Costing"),
        "programmes": ("B.Com", "BBA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2022, "available": True,
    },
    {
        "book_id": "B006", "title": "Financial Management", "author": "I. M. Pandey",
        "subject": "Financial Management",
        "topics": ("Capital Budgeting", "Working Capital", "Cost of Capital"),
        "programmes": ("B.Com", "BBA", "MBA"), "level": "Advanced",
        "book_type": "Reference", "year": 2021, "available": True,
    },
    {
        "book_id": "B007", "title": "Investment Analysis", "author": "Prasanna Chandra",
        "subject": "Investment Management",
        "topics": ("Portfolio Management", "Security Analysis", "Risk and Return"),
        "programmes": ("B.Com", "BBA", "MBA"), "level": "Advanced",
        "book_type": "Research", "year": 2024, "available": True,
    },
    {
        "book_id": "B008", "title": "Principles of Marketing", "author": "Philip Kotler",
        "subject": "Marketing Management",
        "topics": ("Market Segmentation", "Consumer Behaviour", "Marketing Mix"),
        "programmes": ("BBA", "MBA"), "level": "Beginner",
        "book_type": "Textbook", "year": 2022, "available": True,
    },
    {
        "book_id": "B009", "title": "Organisational Behaviour", "author": "Stephen P. Robbins",
        "subject": "Human Resource Management",
        "topics": ("Leadership", "Motivation", "Group Behaviour"),
        "programmes": ("BBA", "MBA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2020, "available": False,
    },
    {
        "book_id": "B010", "title": "Business Statistics", "author": "S. C. Gupta",
        "subject": "Business Statistics",
        "topics": ("Probability", "Correlation", "Regression Analysis"),
        "programmes": ("B.Com", "BBA", "MBA"), "level": "Intermediate",
        "book_type": "Supplementary", "year": 2021, "available": True,
    },
    {
        "book_id": "B011", "title": "Principles of Economics", "author": "N. Gregory Mankiw",
        "subject": "Microeconomics", "topics": ("Demand and Supply", "Elasticity", "Market Structures"),
        "programmes": ("B.Com", "BBA", "BA Economics"), "level": "Beginner",
        "book_type": "Textbook", "year": 2023, "available": True,
    },
    {
        "book_id": "B012", "title": "Macroeconomics", "author": "Dornbusch and Fischer",
        "subject": "Macroeconomics", "topics": ("National Income", "Inflation", "Monetary Policy"),
        "programmes": ("B.Com", "BBA", "BA Economics"), "level": "Intermediate",
        "book_type": "Reference", "year": 2019, "available": True,
    },
    {
        "book_id": "B013", "title": "Introduction to Algorithms", "author": "Cormen et al.",
        "subject": "Data Structures and Algorithms",
        "topics": ("Sorting", "Searching", "Graph Algorithms"),
        "programmes": ("BSc CS", "BCA", "MCA"), "level": "Advanced",
        "book_type": "Reference", "year": 2022, "available": True,
    },
    {
        "book_id": "B014", "title": "Python Programming", "author": "John Zelle",
        "subject": "Programming in Python",
        "topics": ("Data Types", "Functions", "Lists and Dictionaries"),
        "programmes": ("BSc CS", "BCA"), "level": "Beginner",
        "book_type": "Textbook", "year": 2023, "available": True,
    },
    {
        "book_id": "B015", "title": "Database System Concepts", "author": "Silberschatz et al.",
        "subject": "Database Management Systems",
        "topics": ("SQL", "Normalization", "Transactions"),
        "programmes": ("BSc CS", "BCA", "MCA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2020, "available": False,
    },
    {
        "book_id": "B016", "title": "Computer Networks", "author": "Andrew S. Tanenbaum",
        "subject": "Computer Networks",
        "topics": ("OSI Model", "TCP/IP", "Network Security"),
        "programmes": ("BSc CS", "BCA", "MCA"), "level": "Advanced",
        "book_type": "Reference", "year": 2021, "available": True,
    },
    {
        "book_id": "B017", "title": "Operating System Concepts", "author": "Silberschatz et al.",
        "subject": "Operating Systems",
        "topics": ("Process Management", "Memory Management", "Deadlocks"),
        "programmes": ("BSc CS", "BCA", "MCA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2022, "available": True,
    },
    {
        "book_id": "B018", "title": "Discrete Mathematics", "author": "Kenneth H. Rosen",
        "subject": "Discrete Mathematics",
        "topics": ("Logic", "Set Theory", "Graph Theory"),
        "programmes": ("BSc CS", "BCA", "BSc Mathematics"), "level": "Intermediate",
        "book_type": "Supplementary", "year": 2019, "available": True,
    },
    {
        "book_id": "B019", "title": "English Literature: A Guide", "author": "David Daiches",
        "subject": "English Literature",
        "topics": ("Literary Criticism", "Poetry", "Drama"),
        "programmes": ("BA English",), "level": "Beginner",
        "book_type": "Textbook", "year": 2018, "available": True,
    },
    {
        "book_id": "B020", "title": "A Glossary of Literary Terms", "author": "M. H. Abrams",
        "subject": "Literary Studies",
        "topics": ("Literary Criticism", "Narrative", "Figures of Speech"),
        "programmes": ("BA English", "MA English"), "level": "Intermediate",
        "book_type": "Reference", "year": 2020, "available": True,
    },
    {
        "book_id": "B021", "title": "Research Methodology", "author": "C. R. Kothari",
        "subject": "Research Methodology",
        "topics": ("Research Design", "Sampling", "Data Collection"),
        "programmes": ("B.Com", "BBA", "BSc CS", "MA English", "MBA"), "level": "Advanced",
        "book_type": "Research", "year": 2022, "available": True,
    },
    {
        "book_id": "B022", "title": "Business Law", "author": "N. D. Kapoor",
        "subject": "Business Law",
        "topics": ("Contract Act", "Sale of Goods", "Company Law"),
        "programmes": ("B.Com", "BBA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2021, "available": False,
    },
    {
        "book_id": "B023", "title": "Auditing and Assurance", "author": "A. K. Singh",
        "subject": "Auditing", "topics": ("Audit Planning", "Internal Control", "Audit Report"),
        "programmes": ("B.Com", "M.Com"), "level": "Advanced",
        "book_type": "Reference", "year": 2023, "available": True,
    },
    {
        "book_id": "B024", "title": "Entrepreneurship Development", "author": "S. S. Khanka",
        "subject": "Entrepreneurship", "topics": ("Business Plan", "Startup Finance", "Innovation"),
        "programmes": ("BBA", "MBA", "B.Com"), "level": "Beginner",
        "book_type": "Supplementary", "year": 2022, "available": True,
    },
    {
        "book_id": "B025", "title": "Human Resource Management", "author": "Gary Dessler",
        "subject": "Human Resource Management", "topics": ("Recruitment", "Training", "Performance Appraisal"),
        "programmes": ("BBA", "MBA"), "level": "Advanced",
        "book_type": "Reference", "year": 2024, "available": True,
    },
    {
        "book_id": "B026", "title": "Principles of Banking", "author": "M. N. Gopinath",
        "subject": "Banking and Insurance", "topics": ("Central Banking", "Credit Creation", "Insurance"),
        "programmes": ("B.Com", "BBA"), "level": "Intermediate",
        "book_type": "Textbook", "year": 2019, "available": True,
    },
    {
        "book_id": "B027", "title": "Corporate Finance", "author": "Jonathan Berk",
        "subject": "Financial Management", "topics": ("Capital Budgeting", "Valuation", "Capital Structure"),
        "programmes": ("BBA", "MBA", "B.Com"), "level": "Advanced",
        "book_type": "Research", "year": 2024, "available": False,
    },
    {
        "book_id": "B028", "title": "Statistics for Business and Economics", "author": "Anderson et al.",
        "subject": "Business Statistics", "topics": ("Probability", "Hypothesis Testing", "Regression Analysis"),
        "programmes": ("B.Com", "BBA"), "level": "Advanced",
        "book_type": "Reference", "year": 2023, "available": True,
    },
    {
        "book_id": "B029", "title": "Web Technologies", "author": "Uttam K. Roy",
        "subject": "Web Development", "topics": ("HTML", "CSS", "JavaScript"),
        "programmes": ("BSc CS", "BCA"), "level": "Beginner",
        "book_type": "Supplementary", "year": 2021, "available": True,
    },
    {
        "book_id": "B030", "title": "Artificial Intelligence: A Modern Approach", "author": "Russell and Norvig",
        "subject": "Artificial Intelligence", "topics": ("Search Algorithms", "Knowledge Representation", "Reasoning"),
        "programmes": ("BSc CS", "BCA", "MCA"), "level": "Advanced",
        "book_type": "Reference", "year": 2021, "available": True,
    },
]


# Purpose-to-book-type mapping. A direct type match is also accepted.
PURPOSE_TYPES = {
    "study": ("Textbook", "Supplementary"),
    "reference": ("Reference",),
    "research": ("Research", "Reference"),
    "supplementary learning": ("Supplementary", "Textbook"),
}

PROGRAMMES = ("B.Com", "BBA", "BSc CS", "BCA", "M.Com", "MBA", "MCA",
              "BA English", "MA English", "BA Economics", "BSc Mathematics")
LEVELS = ("Beginner", "Intermediate", "Advanced")
PURPOSES = ("Study", "Reference", "Research", "Supplementary learning")


# ---------------------------------------------------------------------------
# Utility and validation functions
# ---------------------------------------------------------------------------

def normalize(value: str) -> str:
    """Return trimmed, case-insensitive text for comparisons."""
    return value.strip().casefold()


def prompt_non_empty(label: str) -> str:
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Please enter a value. This field cannot be empty.")


def choose_from_list(label: str, options: Tuple[str, ...]) -> str:
    """Display numbered options and return the selected option."""
    print(f"\n{label}")
    for index, option in enumerate(options, start=1):
        print(f"  {index}. {option}")
    while True:
        choice = input("Enter choice number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"Enter a number between 1 and {len(options)}.")


def prompt_semester() -> str:
    """Validate a semester value from 1 to 12."""
    while True:
        value = input("Semester (1-12): ").strip()
        if value.isdigit() and 1 <= int(value) <= 12:
            return f"Semester {int(value)}"
        print("Please enter a valid semester number from 1 to 12.")


def collect_student_requirements() -> Dict[str, str]:
    """Collect and validate all academic requirements from the student."""
    print("\n" + "=" * 64)
    print("             STUDENT ACADEMIC REQUIREMENTS")
    print("=" * 64)
    programme = choose_from_list("Select your programme:", PROGRAMMES)
    semester = prompt_semester()
    subject = prompt_non_empty("Enter subject name: ")
    topic = prompt_non_empty("Enter topic: ")
    level = choose_from_list("Select academic difficulty level:", LEVELS)
    purpose = choose_from_list("Select your reading purpose:", PURPOSES)
    return {
        "programme": programme,
        "semester": semester,
        "subject": subject,
        "topic": topic,
        "level": level,
        "purpose": purpose,
    }


# ---------------------------------------------------------------------------
# Required assignment functions
# ---------------------------------------------------------------------------

def display_library() -> None:
    """Display every book in the library catalogue."""
    print("\n" + "=" * 100)
    print(f"{'ID':<7} {'TITLE':<34} {'AUTHOR':<23} {'SUBJECT':<27} {'STATUS':<12}")
    print("-" * 100)
    for book in LIBRARY:
        status = "Available" if book["available"] else "Issued"
        print(f"{book['book_id']:<7} {book['title'][:32]:<34} "
              f"{book['author'][:21]:<23} {book['subject'][:25]:<27} {status:<12}")
    print("-" * 100)
    print(f"Total books in catalogue: {len(LIBRARY)}")


def search_books() -> List[Dict]:
    """Search the catalogue by subject, author, topic, programme or book type."""
    fields = ("Subject", "Author", "Topic", "Programme", "Book type")
    field = choose_from_list("Search books by:", fields)
    query = normalize(prompt_non_empty("Enter search term: "))
    key_map = {
        "Subject": "subject",
        "Author": "author",
        "Topic": "topics",
        "Programme": "programmes",
        "Book type": "book_type",
    }
    key = key_map[field]
    matches = []
    for book in LIBRARY:
        value = book[key]
        if isinstance(value, tuple):
            found = any(query in normalize(item) for item in value)
        else:
            found = query in normalize(str(value))
        if found:
            matches.append(book)
    print_book_list(matches, heading=f"SEARCH RESULTS: {field}")
    return matches


def calculate_score(book: Dict, student_requirements: Dict[str, str]) -> int:
    """
    Calculate a book's score using the assignment's six rules.
    Maximum possible score: 17.
    """
    score = 0
    if normalize(book["subject"]) == normalize(student_requirements["subject"]):
        score += 5
    if any(normalize(student_requirements["topic"]) in normalize(topic)
           for topic in book["topics"]):
        score += 4
    if any(normalize(student_requirements["programme"]) == normalize(programme)
           for programme in book["programmes"]):
        score += 2
    if normalize(book["level"]) == normalize(student_requirements["level"]):
        score += 3

    purpose = normalize(student_requirements["purpose"])
    accepted_types = PURPOSE_TYPES.get(purpose, ())
    if (normalize(book["book_type"]) == purpose
            or any(normalize(book["book_type"]) == normalize(item)
                   for item in accepted_types)):
        score += 2
    if book["available"]:
        score += 1
    return score


def recommendation_category(score: int) -> str:
    """Classify a recommendation using the assignment's score bands."""
    if 14 <= score <= 17:
        return "Highly Recommended"
    elif 10 <= score <= 13:
        return "Recommended"
    elif 6 <= score <= 9:
        return "Moderately Relevant"
    elif 1 <= score <= 5:
        return "Low Relevance"
    else:
        return "Not Relevant"


def explain_recommendation(book: Dict, student_requirements: Dict[str, str]) -> List[str]:
    """Return human-readable reasons for the points awarded to a book."""
    reasons = []
    if normalize(book["subject"]) == normalize(student_requirements["subject"]):
        reasons.append("Exact subject match (+5)")
    if any(normalize(student_requirements["topic"]) in normalize(topic)
           for topic in book["topics"]):
        reasons.append("Requested topic is covered (+4)")
    if any(normalize(student_requirements["programme"]) == normalize(programme)
           for programme in book["programmes"]):
        reasons.append("Programme match (+2)")
    if normalize(book["level"]) == normalize(student_requirements["level"]):
        reasons.append("Difficulty level match (+3)")
    purpose = normalize(student_requirements["purpose"])
    accepted_types = PURPOSE_TYPES.get(purpose, ())
    if (normalize(book["book_type"]) == purpose
            or any(normalize(book["book_type"]) == normalize(item)
                   for item in accepted_types)):
        reasons.append("Reading purpose/book type match (+2)")
    if book["available"]:
        reasons.append("Currently available (+1)")
    if not reasons:
        reasons.append("No recommendation criteria matched.")
    return reasons


def print_book_list(books: List[Dict], heading: str = "BOOKS") -> None:
    """Print a consistent, readable list of book records."""
    print(f"\n{heading}")
    print("-" * 78)
    if not books:
        print("No matching books found.")
        return
    for index, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Issued"
        topics = ", ".join(book["topics"])
        print(f"{index}. {book['title']} [{book['book_id']}]")
        print(f"   Author: {book['author']} | Subject: {book['subject']}")
        print(f"   Topics: {topics}")
        print(f"   Programme(s): {', '.join(book['programmes'])}")
        print(f"   Level: {book['level']} | Type: {book['book_type']} | "
              f"Year: {book['year']} | Status: {status}")
        print("-" * 78)


def display_recommendation_details(recommendations: List[Dict]) -> None:
    """Display rank, book details, score, category and explanation."""
    if not recommendations:
        print("\nNo relevant recommendations were found.")
        return
    print("\n" + "=" * 78)
    print("                    RANKED BOOK RECOMMENDATIONS")
    print("=" * 78)
    for rank, item in enumerate(recommendations, start=1):
        book = item["book"]
        status = "Available" if book["available"] else "Issued"
        print(f"\nRANK {rank} - {book['title']}")
        print(f"Book ID: {book['book_id']}")
        print(f"Author: {book['author']}")
        print(f"Subject: {book['subject']}")
        print(f"Topics: {', '.join(book['topics'])}")
        print(f"Book type: {book['book_type']}")
        print(f"Availability: {status}")
        print(f"Recommendation score: {item['score']}/17")
        print(f"Category: {item['category']}")
        print("Reason for recommendation:")
        for reason in item["reasons"]:
            print(f"  - {reason}")
        print("-" * 78)


def print_summary(all_results: List[Dict], relevant_results: List[Dict]) -> None:
    """Print catalogue evaluation statistics and execution timestamp."""
    total = len(all_results)
    scores = [item["score"] for item in all_results]
    highest = max(scores, default=0)
    average = sum(scores) / total if total else 0
    highly = sum(1 for item in relevant_results if item["score"] >= 14)
    available = sum(1 for item in all_results if item["book"]["available"])
    print("\n" + "=" * 64)
    print("                 RECOMMENDATION SUMMARY")
    print("=" * 64)
    print(f"Execution date and time : {datetime.now().astimezone().strftime('%d-%m-%Y %I:%M:%S %p %Z')}")
    print(f"Total books examined    : {total}")
    print(f"Total relevant books    : {len(relevant_results)}")
    print(f"Highly recommended      : {highly}")
    print(f"Currently available     : {available}")
    print(f"Highest recommendation  : {highest}/17")
    print(f"Average score           : {average:.2f}/17")
    print("=" * 64)


def recommend_books(student_requirements: Dict[str, str],
                    top_n: Optional[int] = None,
                    available_only: bool = False) -> List[Dict]:
    """
    Evaluate the entire catalogue, rank relevant books and display top N.
    List sorting uses a lambda function; top-N uses list slicing.
    """
    all_results = []
    for book in LIBRARY:
        score = calculate_score(book, student_requirements)
        all_results.append({
            "book": book,
            "score": score,
            "category": recommendation_category(score),
            "reasons": explain_recommendation(book, student_requirements),
        })

    relevant = [item for item in all_results if item["score"] > 0]
    if available_only:
        relevant = [item for item in relevant if item["book"]["available"]]

    relevant.sort(key=lambda item: (
        item["score"],
        item["book"]["available"],
        item["book"]["year"],
        item["book"]["title"].casefold(),
    ), reverse=True)

    displayed = relevant[:top_n] if top_n is not None else relevant
    display_recommendation_details(displayed)
    print_summary(all_results, relevant)
    return displayed


# ---------------------------------------------------------------------------
# Additional assignment features
# ---------------------------------------------------------------------------

def subject_wise_recommendations() -> List[Dict]:
    """Display all catalogue books matching a subject, ranked by relevance."""
    subject = prompt_non_empty("Enter subject name: ")
    matches = [book for book in LIBRARY
               if normalize(book["subject"]) == normalize(subject)]
    matches.sort(key=lambda book: (book["available"], book["year"]), reverse=True)
    print_book_list(matches, heading=f"SUBJECT-WISE RESULTS: {subject}")
    return matches


def topic_wise_search() -> List[Dict]:
    """Find books whose topic list contains the requested topic."""
    topic = prompt_non_empty("Enter topic to search: ")
    matches = [
        book for book in LIBRARY
        if any(normalize(topic) in normalize(item) for item in book["topics"])
    ]
    matches.sort(key=lambda book: (book["available"], book["year"]), reverse=True)
    print_book_list(matches, heading=f"TOPIC-WISE RESULTS: {topic}")
    return matches


def prompt_top_n(maximum: int) -> int:
    """Validate how many recommendations the student wants to see."""
    while True:
        value = input(f"Number of recommendations (1-{maximum}): ").strip()
        if value.isdigit() and 1 <= int(value) <= maximum:
            return int(value)
        print(f"Enter a number between 1 and {maximum}.")


def recommendation_workflow() -> None:
    """Run the complete student recommendation process."""
    requirements = collect_student_requirements()
    print("\nAvailability filter:")
    print("1. Show all relevant books")
    print("2. Show only available books")
    while True:
        filter_choice = input("Choose 1 or 2: ").strip()
        if filter_choice in ("1", "2"):
            break
        print("Please enter 1 or 2.")
    top_n = prompt_top_n(len(LIBRARY))
    recommend_books(
        requirements,
        top_n=top_n,
        available_only=(filter_choice == "2"),
    )


def display_menu() -> None:
    """Display the main application menu."""
    print("\n" + "=" * 64)
    print("       UNIVERSITY LIBRARY BOOK RECOMMENDATION SYSTEM")
    print("=" * 64)
    print("1. Get personalized book recommendations")
    print("2. Display complete library catalogue")
    print("3. Search books")
    print("4. Subject-wise book search")
    print("5. Topic-wise book search")
    print("6. Exit")


def main() -> None:
    """Application entry point."""
    print("\nWelcome to the University Library Book Recommendation System!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            recommendation_workflow()
        elif choice == "2":
            display_library()
        elif choice == "3":
            search_books()
        elif choice == "4":
            subject_wise_recommendations()
        elif choice == "5":
            topic_wise_search()
        elif choice == "6":
            print("\nThank you for using the University Library Book Recommendation System.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
