import React from "react";
import { Audio } from "react-loader-spinner";

import "./AudioSpinner.css";

export const AudioSpinner = () => {
  return (
    <div className="loader-overlay">
      <Audio
        height="100"
        width="100"
        color="#4fa94d"
        ariaLabel="audio-loading"
        wrapperStyle={{}}
        wrapperClass="wrapper-class"
        visible={true}
      />
    </div>
  );
};
