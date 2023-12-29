import React from "react";
import styles from "./DropdownModal.module.css";

const formatObservation = (observations) => {
  return (
    <div className={styles.observationContainer}>
      <ul className={styles.observationList}>
        {observations.map((item, index) => (
          <li key={index} className={styles.observation}>
            <span className={styles.number}>{`${index + 1}.`}</span>
            <span
              className={styles.content}
            >{`${item.sender} → ${item.recipient}: `}</span>
            <span className={styles.message}>{item.message}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

const formatHistory = (history) => {
  return Object.keys(history).map((sender) => (
    <div key={sender} className={styles.history}>
      <p>
        <strong>{`${sender}'s`}</strong> previous history with:
      </p>
      {Object.keys(history[sender]).map((recipient) => (
        <ul key={recipient} className={styles.historyItem}>
          <li>
            {`${recipient} on `}
            <span className={styles.url}>{history[sender][recipient].url}</span>
            {` (${history[sender][recipient].data[0]}, ${history[sender][recipient].data[1]})`}
          </li>
        </ul>
      ))}
    </div>
  ));
};

const DropdownModal = ({
  isOpen,
  onClose,
  scenario,
  details,
  onStartEvaluation,
}) => {
  if (!isOpen) return null;

  return (
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <h3
          className={styles.header}
        >{`TRAVOS Demo Scenario ${scenario} Details`}</h3>
        <div className={styles.modalBody}>
          <div className={styles.detailsContainer}>
            <h4>Users:</h4>
            <p>{details.users.join(", ")}</p>
            <h4>Observations:</h4>
            {formatObservation(details.observations)}
            <h4>History:</h4>
            {formatHistory(details.history)}
          </div>
        </div>
        <div className={styles.buttonContainer}>
          <button className={styles.closeButton} onClick={onClose}>
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default DropdownModal;
