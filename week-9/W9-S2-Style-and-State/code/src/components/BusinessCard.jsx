import React from 'react';
import './BusinessCard.css';

function BusinessCard({contact}) {

  const {name, position, email, phone, website, photo} = contact;
  return (
    <div className="business-card">
      <div className="photo-placeholder">
        <img src={photo}/>
      </div>
      <div className="contact-info">
        <h2>{name}</h2>
        <p>Position: {position}</p>
        <p>Email: {email}</p>
        <p>Phone: {phone}</p>
        <p>Website: {website}</p>
      </div>
    </div>
  );
}

export default BusinessCard;
