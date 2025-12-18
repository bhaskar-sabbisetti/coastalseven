import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Auth.css";

export default function Login() {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const navigate = useNavigate();

  const submit = async () => {
    if (!form.username || !form.password) {
      alert("Please fill all fields");
      return;
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/login", form);

      // Save JWT token
      localStorage.setItem("token", res.data.access_token);

      alert("Login successful");

      navigate("/books");
    } catch (error) {
      alert("Invalid username or password");
    }
  };

  return (
    <div className="page-container">
      <div className="auth-card">
        <h2>Login</h2>

        <input
          type="text"
          placeholder="Username"
          value={form.username}
          onChange={(e) =>
            setForm({ ...form, username: e.target.value })
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) =>
            setForm({ ...form, password: e.target.value })
          }
        />

        <button className="btn login-btn" onClick={submit}>
          Login
        </button>

        <p className="link-text" onClick={() => navigate("/register")}>
          Don’t have an account? Register
        </p>
      </div>
    </div>
  );
}
