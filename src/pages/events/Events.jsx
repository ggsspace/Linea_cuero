import React from "react";
import "./Events.css";



const Events = () => {
  return (
    <div className="events-page-container">
      <h1 className="events-title">Próximos eventos virtuales</h1>

      <div className="events-grid">
        <div className="event-card">
          <img src="./src/assets/evento1.jpg" alt="Evento 1" />
        </div>

        <div className="event-card">
          <img src="./src/assets/evento2.png" alt="Evento 2" />
        </div>

        
        <div className="event-card">
          <img src="./src/assets/evento2.png" alt="Evento 2" />
        </div>

        <div className="event-card">
          <img src="./src/assets/evento2.png" alt="Evento 2" />
        </div>

        <div className="event-card">
          <img src="./src/assets/evento2.png" alt="Evento 2" />
        </div>

      </div>
    </div>
  );
};

export default Events;