import React from "react";
import { Container, Image } from "react-bootstrap";
import User from "../../../assets/images/avatar.svg"
import Notification from "../../../assets/images/notification.svg"


export const Header = () => {
  return (
    <header className="main-wrap">
      <Container fluid>
          <div className="text-end">
          <Image src={Notification} alt="Notification"/>
            <Image src={User} alt="User" className="ms-5"/>
          </div>
      </Container>
    </header>
  );
};
