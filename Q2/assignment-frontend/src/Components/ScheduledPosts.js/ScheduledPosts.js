import React, { useEffect, useState } from "react";
import {
  Container,
  Row,
  Col,
  Form,
  Button,
  Table,
  Modal,
  FormCheck,
} from "react-bootstrap";
import { Formik, Field } from "formik";
import { getAllSchedules, saveSchedule } from "../../Apis/ApiFunctions";
import { DatePickerComponent } from "../Common/CommonDatePicker/CommonDatePicker";

export const ScheduledPosts = () => {
  const [scheduledPosts, setScheduledPosts] = useState([]);
  useEffect(() => {
    fetchSchedules();
  }, []);

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const fetchSchedules = async () => {
    const response = await getAllSchedules();
    console.log(response)
    setScheduledPosts(response.data);
  };

  return (
    <div className="main-wrap">
      <Container fluid>
        <div className="mb-3 d-flex align-items-center justify-content-between mb">
          <h1>Scheduled</h1>
          <Button
            variant="dark"
            className="btn-lg"
            onClick={() => handleShow()}
          >
            New Schedule
          </Button>
        </div>
        <Table bordered hover size="lg">
          <thead>
            <tr>
              <th>Title</th>
              <th>Text</th>
              <th>Tag</th>
              <th>Url</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {scheduledPosts &&
              scheduledPosts.length > 0 &&
              scheduledPosts.map((post, index) => (
                <tr key={index}>
                  <td>{post.title || "-"}</td>
                  <td>{post.body || "-"}</td>
                  <td>{post.tags || "-"}</td>
                  <td>{post.media || "-"}</td>
                  <td>{post.rule || "-"}</td>
                </tr>
              ))}
          </tbody>
        </Table>
        <Modal
          size="lg"
          show={show}
          onHide={handleClose}
          backdrop="static"
          keyboard={false}
        >
          <Modal.Header closeButton>
            <Modal.Title>Content Publish</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Formik
              initialValues={{
                title: "",
                text: "",
                tags: "",
                url: "",
                file: "",
                schedule_date: "",
                is_one_time: true,
              }}
              onSubmit={async (values, { resetForm }) => {
                // await new Promise((resolve) => setTimeout(resolve, 500));
                // alert(JSON.stringify(values, null, 2));
                const response = await saveSchedule(values);
                handleClose();
                resetForm();
                if (response) {
                  fetchSchedules();
                }
              }}
            >
              {({
                values,
                errors,
                touched,
                handleChange,
                handleBlur,
                handleSubmit,
                isSubmitting,
                setFieldValue,
                /* and other goodies */
              }) => (
                <Form onSubmit={handleSubmit}>
                  <Row>
                    {console.log("values : ", values)}
                    <Col>
                      <Form.Group
                        className="mb-3"
                        controlId="exampleForm.ControlInput1"
                      >
                        <Form.Label>Title</Form.Label>
                        <Form.Control
                          name="title"
                          onChange={handleChange}
                          type="text"
                          placeholder="Enter Title"
                        />
                      </Form.Group>
                    </Col>
                    <Col>
                      <Form.Group
                        className="mb-3"
                        controlId="exampleForm.ControlInput1"
                      >
                        <Form.Label>Tag</Form.Label>
                        <Form.Control
                          name="tags"
                          onChange={handleChange}
                          type="text"
                          placeholder="Enter Tag"
                        />
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      <Form.Group
                        className="mb-3"
                        controlId="exampleForm.ControlInput1"
                      >
                        <Form.Label>Url</Form.Label>
                        <Form.Control
                          name="url"
                          onChange={handleChange}
                          type="text"
                          placeholder="Enter Url"
                        />
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                    <Form.Group
                      className="mb-3"
                      controlId="exampleForm.ControlInput1"
                    >
                      <Form.Label>Text</Form.Label>
                      <Form.Control
                        name="text"
                        onChange={handleChange}
                        as="textarea"
                        type="text"
                        placeholder="Enter text"
                      />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Col>
                      <Form.Group
                        className="mb-3"
                        controlId="exampleForm.ControlInput1"
                      >
                        <Form.Label>File</Form.Label>
                        <Form.Control
                          name="file"
                          onChange={handleChange}
                          type="file"
                          placeholder="Select File"
                        />
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row className="align-items-center">
                    <Col>
                      <Form.Group className="mb-3">
                        <Form.Label>Schedule Date</Form.Label>
                        <Row>
                          <DatePickerComponent
                            name="schedule_date"
                            startDate={values.schedule_date}
                            onChange={(value) =>
                              setFieldValue("schedule_date", value)
                            }
                            disabled={values.is_one_time}
                          />
                        </Row>
                      </Form.Group>
                    </Col>
                    <Col>
                    <Form.Group className="mb-3">
                        <Form.Label className="d-flex space-between">
                          <FormCheck
                            className="me-1"
                            name="is_one_time"
                            onChange={(e) =>
                              setFieldValue("is_one_time", e.target.checked)
                            }
                            checked={values.is_one_time}
                          />
                           Schedule Date
                        </Form.Label>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                      Close
                    </Button>
                    <Button type="submit" variant="dark">Save</Button>
                  </Modal.Footer>
                </Form>
              )}
            </Formik>
          </Modal.Body>
        </Modal>
      </Container>
    </div>
  );
};
