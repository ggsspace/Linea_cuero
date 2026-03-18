import Card from "../../components/card/Card.jsx";
import "./Products.css";
import { productosData } from "./productsData.js";

const Products = () => {
  return (
    <main>
      <section className="products-section">
        <h2 className="products-title">Nuestros Productos</h2>
        <div className="cards-container">
          {productosData.map((product) => (
            <Card key={product.id} {...product} />
          ))}
        </div>
      </section>

      <section className="products-section">
        <div className="cards-container">
          {productosData.map((product) => (
            <div key={product.id} className="card">
              <img src={product.imagen} alt="imagen" />
              <div className="card-body">
                <h3>{product.titulo}</h3>
                <p>{product.descripcion}</p>
                <span>{product.precio}</span>
                <button>Comprar</button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;