import axios from "axios";
import { ApiRoutes } from "./ApiRoutes";

export const getYoutubeTitleData = async () => {
  try {
    const response = await axios.get(ApiRoutes.youtube_details);
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getRedditTitleDetails = async () => {
  try {
    const response = await axios.get(ApiRoutes.reddit_details);
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getRedditBarChartData = async () => {
  try {
    const response = await axios.get(ApiRoutes.reddit_comment_polarity);
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const saveSchedule = async (params) => {
  try {
    const response = await axios.post(ApiRoutes.schedule,  params );
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getAllSchedules = async () => {
  try {
    const response = await axios.get(ApiRoutes.schedule);
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getRedditPredictiveLikes = async (params) => {
  try {
    const response = await axios.get(ApiRoutes.reddit_likes, { params });
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getYoutubePredictiveViews = async (params) => {
  try {
    const response = await axios.get(ApiRoutes.youtube_predictive_views, {
      params,
    });
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};

export const getNetworkAnalysisData = async () => {
  try {
    const response = await axios.get(ApiRoutes.basic_network_properties);
    return response?.data;
  } catch (error) {
    return error?.response;
  }
};
