import React, { useEffect, useState } from "react";
import { Container, Card, Row, Col, Image } from "react-bootstrap";
import "../../App.css";
import { ChartCard } from "../Common/Charts/ChartCard";
import { mockData } from "../../mockData";
import Reddit from "../../assets/images/reddit.svg";
import Youtube from "../../assets/images/youtube.svg";
import Subscribe from "../../assets/images/subscribes.svg";
import Like from "../../assets/images/likes.svg";
import Comments from "../../assets/images/comments.svg";
import {
  getNetworkAnalysisData,
  getRedditBarChartData,
  getRedditPredictiveLikes,
  getRedditTitleDetails,
  getYoutubePredictiveViews,
  getYoutubeTitleData,
} from "../../Apis/ApiFunctions";
import { BasicNetworkProperties } from "./BasicNetworkProperties";
import { AudioSpinner } from "../Common/Spinners/AudioSpinner";

export const Dashboard = () => {
  const [youtubeCountData, setYoutubeCountData] = useState({
    data: null,
    isLoading: false,
  });
  const [redditCountData, setRedditCountData] = useState({
    data: null,
    isLoading: false,
  });
  const [redditCommentPolarityData, setRedditCommentPolarityData] = useState({
    data: null,
    isLoading: false,
  });

  const [redditPredictiveLikeData, setRedditPredictiveLikeData] = useState({
    data: null,
    isLoading: false,
  });
  const [youtubePredictiveViewsData, setYoutubePredictiveViewsData] = useState({
    data: null,
    isLoading: false,
  });
  const [networkAnalysisData, setNetworkAnalysisData] = useState({
    data: null,
    isLoading: false,
  });

  useEffect(() => {
    fetchDashboardCounts();
    fetchRedditPredictiveLikeChartData({ forecast_periods: 7 });
    fetchRedditCommentPolarutyData();
    fetchYoutubePredictiveViewsChartData({ forecast_periods: 7 });
    fetchNetworkAnalysisData();
  }, []);

  const fetchNetworkAnalysisData = async () => {
    setNetworkAnalysisData({ ...networkAnalysisData, isLoading: true });
    const response = await getNetworkAnalysisData();
    if (response) {
      setNetworkAnalysisData({ data: response?.data, isLoading: false });
    }
  };

  const fetchYoutubePredictiveViewsChartData = async (params) => {
    setYoutubePredictiveViewsData({
      ...youtubePredictiveViewsData,
      isLoading: true,
    });
    const response = await getYoutubePredictiveViews(params);
    console.log("response------------", response)
    if (response?.data) {
      setYoutubePredictiveViewsData({ data: response?.data, isLoading: false });
    }
  };

  const fetchRedditPredictiveLikeChartData = async (params) => {
    setRedditPredictiveLikeData({
      ...redditPredictiveLikeData,
      isLoading: true,
    });
    const response = await getRedditPredictiveLikes(params);
    if (response?.data) {
      setRedditPredictiveLikeData({ data: response?.data, isLoading: false });
    }
  };

  const fetchRedditCommentPolarutyData = async () => {
    setRedditCommentPolarityData({
      ...redditCommentPolarityData,
      isLoading: true,
    });
    const response = await getRedditBarChartData();
    if (response) {
      setRedditCommentPolarityData({ data: response?.data, isLoading: false });
    }
  };

  const fetchDashboardCounts = async () => {
    setRedditCountData({ ...redditCountData, isLoading: true });
    setYoutubeCountData({ ...youtubeCountData, isLoading: true });
    const redditCounts = await getRedditTitleDetails();
    if (redditCounts) {
      setRedditCountData({
        data: redditCounts.data,
        isLoading: false,
      });
    }
    const youTubeCounts = await getYoutubeTitleData();

    if (youTubeCounts) {
      setYoutubeCountData({
        data: youTubeCounts.data,
        isLoading: false,
      });
    }
  };

  const handleChartFilter = async (value, isReddit) => {
    if (isReddit) {
      fetchRedditPredictiveLikeChartData({ forecast_periods: value });
    } else {
      fetchYoutubePredictiveViewsChartData({ forecast_periods: value });
    }
  };

  console.log(redditCountData, youtubeCountData);
  return (
    <div className="main-wrap">
      <Container fluid>
        <h1>Starbucks Dashboard</h1>
        <Row className="mt-5">
          <Col md={6}>
            <div className="left-column">
              <div className="section-header d-flex align-items-center mb-5">
                <Image src={Reddit} width="50" />
                <div className="d-block ms-3">
                  <h3 className="mb-0">
                    <b>Reddit</b>
                  </h3>
                  <h4>Performance</h4>
                </div>
              </div>
            </div>
            <div className="action-box-wrap d-flex gap-3 mb-4">
              <Card className="action-box subscribes">
                {redditCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Subscribe} width="50" className="mb-3" />
                    <h4>{redditCountData?.data?.subscriber_count}</h4>
                    <p>Total Subscribers</p>
                  </>
                )}
              </Card>
              <Card className="action-box likes">
                {redditCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Like} width="50" className="mb-3" />
                    <h4>{redditCountData?.data?.like_count}</h4>
                    <p>Total Likes</p>
                  </>
                )}
              </Card>
              <Card className="action-box comments">
                {redditCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Comments} width="50" className="mb-3" />
                    <h4>{redditCountData?.data?.comment_count}</h4>
                    <p>Total comments</p>
                  </>
                )}
              </Card>
            </div>
            {redditPredictiveLikeData && (
              <ChartCard
                className="chart action-box"
                text="Reddit Likes"
                chartData={redditPredictiveLikeData}
                type="line"
                isReddit={true}
                handleChartFilter={handleChartFilter}
                isLoading={redditPredictiveLikeData.isLoading}
                hasFilter={true}
              />
            )}

            {redditCommentPolarityData && (
              <ChartCard
                className="chart action-box"
                text="Redit Comments"
                chartData={redditCommentPolarityData}
                type="bar"
                isLoading={redditCommentPolarityData?.isLoading}
              />
            )}
          </Col>
          <Col md={6}>
            <div className="right-column">
              <div className="section-header d-flex align-items-center mb-5">
                <Image src={Youtube} width="50" />
                <div className="d-block ms-3">
                  <h3 className="mb-0">
                    <b>Youtube</b>
                  </h3>
                  <h4>Performance</h4>
                </div>
              </div>
            </div>
            <div className="action-box-wrap d-flex gap-3 mb-4">
              <Card className="action-box subscribes">
                {youtubeCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Subscribe} width="50" className="mb-3" />
                    <h4>{youtubeCountData?.data?.subscriber_count}</h4>
                    <p>Total Subscribers</p>
                  </>
                )}
              </Card>
              <Card className="action-box likes">
                {youtubeCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Like} width="50" className="mb-3" />
                    <h4>{youtubeCountData?.data?.like_count}</h4>
                    <p>Total Likes</p>
                  </>
                )}
              </Card>
              <Card className="action-box comments">
                {youtubeCountData.isLoading ? (
                  <AudioSpinner />
                ) : (
                  <>
                    <Image src={Comments} width="50" className="mb-3" />
                    <h4>{youtubeCountData?.data?.comment_count}</h4>
                    <p>Total comments</p>
                  </>
                )}
              </Card>
            </div>
            {youtubePredictiveViewsData && (
              <ChartCard
                className="chart action-box"
                text="Youtube Views"
                chartData={youtubePredictiveViewsData}
                type="line"
                isReddit={false}
                handleChartFilter={handleChartFilter}
                isLoading={youtubePredictiveViewsData?.isLoading}
                hasFilter={true}
              />
            )}

            <ChartCard
              className="chart action-box"
              text="Basic Network Properties"
              chartData={networkAnalysisData}
              type="table"
              isReddit={false}
              isLoading={networkAnalysisData?.isLoading}
            />
          </Col>
        </Row>
      </Container>
    </div>
  );
};
