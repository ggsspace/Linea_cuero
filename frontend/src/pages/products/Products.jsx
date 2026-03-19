import "./Products.css";
import { useCart } from "../../context/CartContext.jsx";
import { useState } from "react";

const productsData = [
  {
    id: 1,
    title: "Botines de Cuero",
    description: "Calzado de alta calidad hecho con cuero de alta calidad",
    price: "$120.000",
    oldPrice: "$150.000",
    image: "https://via.placeholder.com/300",
    stock: true,
  },
  {
    id: 2,
    title: "Bolso de Cuero",
    description: "Marroquinería de autor con sello de innovación",
    price: "$80.000",
    oldPrice: "$100.000",
    image: "https://via.placeholder.com/300",
    stock: true,
  },
  {
    id: 3,
    title: "Cinturón Premium",
    description: "Accesorio elegante fabricado a mano",
    price: "$45.000",
    oldPrice: "$60.000",
    image: "https://via.placeholder.com/300",
    stock: true,
  },
  {
    id: 4,
    title: "Chaqueta de Cuero",
    description: "Prenda con sello de innovación y alta resistencia",
    price: "$200.000",
    oldPrice: "$250.000",
    image: "https://via.placeholder.com/300",
    stock: false,
  },
];

const Products = () => {
  const { addToCart } = useCart();
  const [search, setSearch] = useState("");
  const [selected, setSelected] = useState([]);
  const [wishlist, setWishlist] = useState([]);

  const filteredProducts = productsData.filter((product) =>
    product.title.toLowerCase().includes(search.toLowerCase())
  );

  const toggleSelectAll = () => {
    if (selected.length === filteredProducts.length) {
      setSelected([]);
    } else {
      setSelected(filteredProducts.map((p) => p.id));
    }
  };

  const toggleSelect = (id) => {
    setSelected((prev) =>
      prev.includes(id) ? prev.filter((i) => i !== id) : [...prev, id]
    );
  };

  const toggleWishlist = (id) => {
    setWishlist((prev) =>
      prev.includes(id) ? prev.filter((i) => i !== id) : [...prev, id]
    );
  };

  return (
    <main>
      <section className="products-section">
        <h2 className="products-title">Nuestros Productos</h2>

        <div className="products-search">
          <input
            type="text"
            placeholder="Buscar producto..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="search-input"
          />
          <button className="search-btn">Buscar</button>
        </div>

        <div className="products-select-all">
          <input
            type="checkbox"
            checked={selected.length === filteredProducts.length && filteredProducts.length > 0}
            onChange={toggleSelectAll}
          />
          <span>Marcar todos</span>
        </div>

        <div className="cards-container">
          {filteredProducts.map((product) => (
            <div className="card" key={product.id}>
              <div className="card-top">
                <input
                  type="checkbox"
                  checked={selected.includes(product.id)}
                  onChange={() => toggleSelect(product.id)}
                />
                <button
                  className={`wishlist-btn ${wishlist.includes(product.id) ? "active" : ""}`}
                  onClick={() => toggleWishlist(product.id)}
                >
                  ♡
                </button>
              </div>

              <img src={product.image} alt={product.title} />

              <div className="card-body">
                <span className={`stock-badge ${product.stock ? "in-stock" : "out-stock"}`}>
                  {product.stock ? "Stock disponible" : "Sin stock"}
                </span>
                <h3>{product.title}</h3>
                <div className="card-prices">
                  <span className="card-price">{product.price}</span>
                  <span className="card-old-price">{product.oldPrice}</span>
                </div>
                <p>{product.description}</p>
                <div className="card-actions">
                  <button
                    className="card-btn-primary"
                    onClick={() => addToCart(product)}
                  >
                    Reservar Ahora
                  </button>
                  <button className="card-btn-icon">🗑</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;