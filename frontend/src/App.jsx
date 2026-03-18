import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavBar from "./components/navbar/NavBar.jsx";
import Home from "./pages/home/Home.jsx";
import Products from "./pages/products/Products.jsx";
import Calendar from "./pages/calendar/Calendar.jsx";
import QA from "./pages/qa/QA.jsx";
import LogIn from "./pages/login/LogIn.jsx";
import Cart from "./pages/cart/Cart.jsx";

function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/productos" element={<Products />} />  {/* ← esta */}
        <Route path="/calendario" element={<Calendar />} />
        <Route path="/qa" element={<QA />} />
        <Route path="/login" element={<LogIn />} />
        <Route path="/cart" element={<Cart />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;