import { useEffect, useState } from "react";
import api from "./api";
import "./Books.css";

export default function Books() {
  const [books, setBooks] = useState([]);
  const [form, setForm] = useState({ title: "", author: "", price: "" });
  const [editId, setEditId] = useState(null);

  // Pagination state
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  const limit = 5;

  // Load books with pagination
  const loadBooks = async () => {
    const res = await api.get(`/books?page=${page}&limit=${limit}`);
    setBooks(res.data.books);  
    setTotal(res.data.total);  
  };

  useEffect(() => {
    loadBooks();
  }, [page]);

  // Add or update book
  const submit = async () => {
    if (!form.title || !form.author || !form.price) return;

    if (editId) {
      await api.put(`/books/${editId}`, form);
      setEditId(null);
    } else {
      await api.post("/books", form);
    }

    setForm({ title: "", author: "", price: "" });
    loadBooks();
  };

  // Edit
  const editBook = (book) => {
    setEditId(book.id);
    setForm({
      title: book.title,
      author: book.author,
      price: book.price,
    });
  };

  // Delete
  const deleteBook = async (id) => {
    await api.delete(`/books/${id}`);
    loadBooks();
  };

  const totalPages = Math.ceil(total / limit);

  return (
    <div className="books-container">
      <h2>Book Store</h2>

      {/* Book Form */}
      <div className="book-form">
        <input
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
        />
        <input
          placeholder="Author"
          value={form.author}
          onChange={(e) => setForm({ ...form, author: e.target.value })}
        />
        <input
          placeholder="Price"
          value={form.price}
          onChange={(e) => setForm({ ...form, price: e.target.value })}
        />
        <button onClick={submit}>
          {editId ? "Update" : "Add"} Book
        </button>
      </div>

      {/* Books Table */}
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {books.map((b) => (
            <tr key={b.id}>
              <td>{b.title}</td>
              <td>{b.author}</td>
              <td>₹{b.price}</td>
              <td>
                <button onClick={() => editBook(b)}>Edit</button>
                <button onClick={() => deleteBook(b.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination */}
      <div className="pagination">
        <button
          disabled={page === 1}
          onClick={() => setPage(page - 1)}
        >
          Prev
        </button>

        <span>
          Page {page} of {totalPages || 1}
        </span>

        <button
          disabled={page === totalPages || totalPages === 0}
          onClick={() => setPage(page + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}
