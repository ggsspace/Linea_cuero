import Card from "../../components/card/Card.jsx";
import productos from "./Products.js"; 
import "./Products.css";

const Products = () => {
  return (
    <main>
      <section className="productos-section">
        <h2 className="productos-titulo">Nuestros Productos</h2>
        <div className="cards-container">
          {productos.map((producto) => (
            <Card key={producto.id} {...producto} />
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;