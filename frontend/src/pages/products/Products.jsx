import "./Products.css";
import { useCart } from "../../context/CartContext.jsx"; // Conecta el carrito al componente

const productsData = [
  {
    id: 1,
    title: "Product 1",
    description: "Product description",
    price: "$10.000",
    image: "https://via.placeholder.com/300"
  },
  {
    id: 2,
    title: "Product 2",
    description: "Product description",
    price: "$20.000",
    image: "https://via.placeholder.com/300"
  },
  {
    id: 3,
    title: "Product 3",
    description: "Product description",
    price: "$30.000",
    image: "https://via.placeholder.com/300"
  }
];

const Products = () => {
  const { addToCart } = useCart();

  return (
    <main>
      <section className="products-section">
        <h2 className="products-title">Nuestros Productos</h2>
        <div className="cards-container">
          {productsData.map((product) => (
            <div className="card" key={product.id}>
              <img src={product.image} alt={product.title} />
              <div className="card-body">
                <h3>{product.title}</h3>
                <p>{product.description}</p>
                <span>{product.price}</span>
                <button onClick={() => addToCart(product)}>Comprar</button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;