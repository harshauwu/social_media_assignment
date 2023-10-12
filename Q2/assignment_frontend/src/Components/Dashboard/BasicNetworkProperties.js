import React from "react";
import { Table } from "react-bootstrap";

export const BasicNetworkProperties = ({data}) => {
  console.log('&&&&&&&&&&&&&&')
  console.log(data)
 
  return (
  <>{data &&
    <div>
      <ul>
        {Object.keys(
          data.basic_network_properties
        ).map((key, index) => {
          console.log(
            data.basic_network_properties
          );
          return (
            <li className="d-flex">
              <strong>{key.replace("_", " ").toLocaleUpperCase()}</strong>
              <p style={{ paddingLeft: "6px" }}>
                {data.basic_network_properties[key]}
              </p>
            </li>
          );
        })}
      </ul>
      <h5 style={{marginTop: "1em"}}>Centrality Measurement</h5>
      <Table striped bordered hover responsive>
        <thead>
          <tr>
            <th colSpan={2}>Degree Centrality</th>
            <th colSpan={2}>Closeness Centrality</th>
            <th colSpan={2}>Betweeness Centrality</th>
          </tr>
          <tr>
            <th>Author</th>
            <th>Centrality</th>
            <th>Author</th>
            <th>Centrality</th>
            <th>Author</th>
            <th>Centrality</th>
          </tr>
        </thead>
        <tbody>
          {data && [1,2,3,4,5].map((y, x) => (
            <tr>
              <td>
                {" "}
                {data.degree_centrality[x].node}
              </td>{" "}
              <td>
                {
                  data.degree_centrality[x]
                    .centrality
                }
              </td>
              <td>
                {data.closeness_centrality[x].node}
              </td>{" "}
              <td>
                {
                  data.closeness_centrality[x]
                    .centrality
                }
              </td>
              <td>
                {" "}
                {
                  data.betweenness_centrality[x]
                    .node
                }
              </td>{" "}
              <td>
                {
                  data.betweenness_centrality[x]
                    .centrality
                }
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
}</>);
};
