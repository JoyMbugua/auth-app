import React, { Component } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "",
      loggedin: false,
    };
    this.getMessage = this.getMessage.bind(this);
  }

  async getMessage() {
    try {
      const header = localStorage.getItem("access_token");
   
      await axios
        .get("http://127.0.0.1:8000/api/v1/dashboard/", {
          headers: {
            Authorization: "JWT " + localStorage.getItem("access_token"),
            "Content-Type": "application/json",
            accept: "application/json",
          },
        })
        .then((resp) => resp)
        .then((data) => {
          const message = data.data.message;
          this.setState({
            message: message,
            loggedin: true,
          });
          return message;
        });
    } catch (error) {
      throw error;
    }
  }
  componentDidMount() {
    const msg = this.getMessage();
    // console.log("message", JSON.stringify(msg, null, 4));
  }

  render() {
    return (
      <div>
        <h1 className="centered-text">{this.state.message}</h1> <br />
        {this.state.loggedin && (
          <Link className="logoutinputs" to={"/logout/"}>
            <input type="submit" value="Logout" />
          </Link>
        )}
      </div>
    );
  }
}
export default Dashboard;
