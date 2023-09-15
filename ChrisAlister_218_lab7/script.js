document.addEventListener("DOMContentLoaded", function () {
    // Get references to DOM elements
    const fetchBooksButton = document.getElementById("fetchBooks");
    const bookListDiv = document.getElementById("bookList");

    // Add a click event listener to the "Fetch Books" button
    fetchBooksButton.addEventListener("click", function () {
        // Make an AJAX request to fetch the JSON data
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "https://jsonplaceholder.typicode.com/posts", true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    try {
                        // Parse the JSON response
                        const response = JSON.parse(xhr.responseText);
                        // Display the fetched books
                        displayBooks(response);
                    } catch (error) {
                        bookListDiv.innerHTML = "Error parsing JSON data.";
                    }
                } else {
                    bookListDiv.innerHTML = "Error fetching data.";
                }
            }
        };
        xhr.send();
    });

    // Function to display the fetched books
    function displayBooks(books) {
        // Clear any previous book list
        bookListDiv.innerHTML = "";

        // Check if 'books' is an array
        if (Array.isArray(books)) {
            if (books.length === 0) {
                bookListDiv.innerHTML = "No books found.";
            } else {
                // Create a list of books
                const ul = createBookList(books);
                bookListDiv.appendChild(ul);
            }
        } else {
            bookListDiv.innerHTML = "Invalid data format.";
        }
    }

    // Function to create a list of books
    function createBookList(books) {
        const ul = document.createElement("ul");
        books.forEach(function (book) {
            if (book && book.title) {
                const li = document.createElement("li");
                li.textContent = book.title;
                ul.appendChild(li);
            }
        });
        return ul;
    }
});
