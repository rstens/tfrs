import axios from 'axios';

import * as ActionTypes from '../constants/actionTypes';
import * as Routes from '../constants/routes';

/*
 * Credit Transfers
 */
export const getCreditTransfers = () => (dispatch) => {
  dispatch(getCreditTransfersRequest());
  return axios.get(Routes.BASE_URL + Routes.CREDIT_TRADE_API)
    .then((response) => {
      dispatch(getCreditTransfersSuccess(response.data));
    }).catch((error) => {
      dispatch(getCreditTransfersError(error.response));
    });
};

export const shouldGetCreditTransfers = (state) => {
  const { creditTransfers } = state;
  if (!creditTransfers) {
    return true;
  } else if (creditTransfers.isFetching) {
    return false;
  }
  return creditTransfers.didInvalidate;
};

export const getCreditTransfersIfNeeded = () =>
  (dispatch, getState) => {
    if (shouldGetCreditTransfers(getState())) {
      // Dispatch a thunk from thunk!
      return dispatch(getCreditTransfers());
    }
    // Let the calling code know there's nothing to wait for.
    return Promise.resolve();
  };

const getCreditTransfersRequest = () => ({
  name: 'GET_CREDIT_TRANSFERS_REQUEST',
  type: ActionTypes.GET_CREDIT_TRANSFERS
});

const getCreditTransfersSuccess = creditTransfers => ({
  name: 'RECEIVE_CREDIT_TRANSFERS_REQUEST',
  type: ActionTypes.RECEIVE_CREDIT_TRANSFERS,
  data: creditTransfers,
  receivedAt: Date.now()
});

const getCreditTransfersError = error => ({
  name: 'ERROR_CREDIT_TRANSFERS_REQUEST',
  type: ActionTypes.ERROR,
  errorMessage: error
});

export const invalidateCreditTransfers = creditTransfers => ({
  type: ActionTypes.INVALIDATE_CREDIT_TRANSFERS,
  data: creditTransfers
});

/*
 * Credit Transfer Detail
 */
export const getCreditTransfer = id => (dispatch) => {
  dispatch(getCreditTransferRequest());
  return axios.get(`${Routes.BASE_URL}${Routes.CREDIT_TRADE_API}/${id}`)
    .then((response) => {
      dispatch(getCreditTransferSuccess(response.data));
    }).catch((error) => {
      dispatch(getCreditTransferError(error.response));
    });
};

export const shouldGetCreditTransfer = (state) => {
  const { creditTransfer } = state;
  if (!creditTransfer) {
    return true;
  } else if (creditTransfer.isFetching) {
    return false;
  }
  return creditTransfer.didInvalidate;
};

export const getCreditTransferIfNeeded = id =>
  (dispatch, getState) => {
    if (shouldGetCreditTransfer(getState())) {
      // Dispatch a thunk from thunk!
      return dispatch(getCreditTransfer(id));
    }
    // Let the calling code know there's nothing to wait for.
    return Promise.resolve();
  };

const getCreditTransferRequest = () => ({
  name: 'GET_CREDIT_TRANSFER_REQUEST',
  type: ActionTypes.GET_CREDIT_TRANSFER
});

const getCreditTransferSuccess = creditTransfer => ({
  name: 'RECEIVE_CREDIT_TRANSFER_REQUEST',
  type: ActionTypes.RECEIVE_CREDIT_TRANSFER,
  data: creditTransfer,
  receivedAt: Date.now()
});

const getCreditTransferError = error => ({
  name: 'ERROR_CREDIT_TRANSFER_REQUEST',
  type: ActionTypes.ERROR,
  errorMessage: error
});

export const invalidateCreditTransfer = creditTransfer => ({
  type: ActionTypes.INVALIDATE_CREDIT_TRANSFER,
  data: creditTransfer
});

/*
 * Add Credit Transfers
 */
export const addCreditTransfer = data => (dispatch) => {
  dispatch(addCreditTransferRequest());
  return axios
    .post(Routes.BASE_URL + Routes.CREDIT_TRADE_API, data)
    .then((response) => {
      dispatch(addCreditTransferSuccess(response.data));
    }).catch((error) => {
      dispatch(addCreditTransferError(error.response.data));
    });
};

const addCreditTransferRequest = () => ({
  name: 'ADD_CREDIT_TRANSFER',
  type: ActionTypes.ADD_CREDIT_TRANSFER
});

const addCreditTransferSuccess = data => ({
  name: 'SUCCESS_ADD_CREDIT_TRANSFER',
  type: ActionTypes.SUCCESS_ADD_CREDIT_TRANSFER,
  data
});

const addCreditTransferError = error => ({
  name: 'ERROR_ADD_CREDIT_TRANSFER',
  type: ActionTypes.ERROR,
  errorMessage: error
});

/*
 * Edit/Update credit transfer
 */
export const updateCreditTransfer = (id, data) => (dispatch) => {
  dispatch(updateCreditTransferRequest());
  console.log('updating', data);
  return axios
    .put(`${Routes.BASE_URL}${Routes.CREDIT_TRADE_API}/${id}`, data)
    .then((response) => {
      dispatch(updateCreditTransferSuccess(response.data));
    }).catch((error) => {
      dispatch(updateCreditTransferError(error.response.data));
    });
};

const updateCreditTransferRequest = () => ({
  name: 'UPDATE_CREDIT_TRANSFER',
  type: ActionTypes.REQUEST
});

const updateCreditTransferSuccess = data => ({
  name: 'SUCCESS_UPDATE_CREDIT_TRANSFER',
  type: ActionTypes.SUCCESS,
  data
});

const updateCreditTransferError = error => ({
  name: 'ERROR_ADD_CREDIT_TRANSFER',
  type: ActionTypes.ERROR,
  errorMessage: error
});

/*
 * Delete credit transfer
 */
export const deleteCreditTransfer = data => (dispatch) => {
  dispatch(deleteCreditTransferRequest());
  axios
    .post(Routes.BASE_URL + Routes.CREDIT_TRADE_API, data)
    .then((response) => {
      dispatch(deleteCreditTransferSuccess(response.data));
    }).catch((error) => {
      dispatch(deleteCreditTransferError(error.response.data));
    });
};

const deleteCreditTransferRequest = () => ({
  name: 'UPDATE_CREDIT_TRANSFER',
  type: ActionTypes.REQUEST
});

const deleteCreditTransferSuccess = data => ({
  name: 'SUCCESS_UPDATE_CREDIT_TRANSFER',
  type: ActionTypes.SUCCESS,
  data
});

const deleteCreditTransferError = error => ({
  name: 'ERROR_ADD_CREDIT_TRANSFER',
  type: ActionTypes.ERROR,
  errorMessage: error
});
