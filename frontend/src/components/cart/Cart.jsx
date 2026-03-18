function Card({ imagen, titulo, descripcion, precio }) {
  return (
    <div className="card">
      <img src={imagen} alt={titulo} />
      <div className="card-body">
        <h3>{titulo}</h3>
        <p>{descripcion}</p>
        <span>{precio}</span>
        <button>Comprar</button>
      </div>
    </div>
  );
}

export default Card;

function Cart({ imagen, titulo, descripcion, precio }) {
  return (
    <div className="cart">
      <img src={imagen} alt="imagen" />
      <div className="cart-body">
        <h3>{titulo}</h3>
        <p>{descripcion}</p>
        <span>{precio}</span>
        <button>Comprar</button>
      </div>
    </div>
  );
}

export { Cart };