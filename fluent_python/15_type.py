from typing import TypedDict, TYPE_CHECKING

class BookDict(TypedDict):
    isbn: str
    title: str 
    authors: list[str]
    pagecount: int


def demo() -> None:
    book = BookDict(
        isbn='38424342',
        title='refactoring',
        authors=['Wathashi me', 'You you'],
        pagecount=123
    )

    authors = book['authors']
    if TYPE_CHECKING:
        reveal_type(authors)
    authors = 'Bob'
    book['weight'] = 4.2 
    del book['title']

if __name__ == '__main__':
    demo()