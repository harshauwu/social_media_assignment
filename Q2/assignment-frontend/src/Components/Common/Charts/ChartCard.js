import React from "react";
import { Card, Dropdown, DropdownButton } from "react-bootstrap";
import { LineChart } from "./LineChart/LineChart";
import { BarChart } from "./BarChart/BarChart";
import { BasicNetworkProperties } from "../../Dashboard/BasicNetworkProperties";
import { AudioSpinner } from "../Spinners/AudioSpinner";

export const ChartCard = ({
  text,
  chartData,
  type,
  className,
  isReddit,
  handleChartFilter,
  isLoading,
  hasFilter,
}) => {
  console.log("chartData ::: ", chartData);
  return (
    <Card className={`mb-4 ${className}`}>
      {isLoading ? (
        <div style={{ height: "634px" }}>
          <AudioSpinner />
        </div>
      ) : (
        <>
          <div className="mb-3 d-flex justify-content-between align-items-center">
            <h5 className="m-0">{text}</h5>
            {hasFilter && (
              <DropdownButton
                variant="success"
                onSelect={(value) => handleChartFilter(value, isReddit)}
                id="dropdown-basic-button"
                title="Period"
              >
                <Dropdown.Item eventKey="7">week</Dropdown.Item>
                <Dropdown.Item eventKey="14">2 weeks</Dropdown.Item>
                <Dropdown.Item eventKey="30">month</Dropdown.Item>
              </DropdownButton>
            )}
          </div>

          {type == "line" ? (
            <div className="white-bg">
              <LineChart data={chartData?.data} isReddit={isReddit} />
            </div>
          ) : type == "bar" ? (
            <div className="white-bg">
              <BarChart data={chartData?.data} />
            </div>
          ) : (
            <div className="white-bg">
              <BasicNetworkProperties data={chartData?.data} />
            </div>
          )}
        </>
      )}
    </Card>
  );
};
