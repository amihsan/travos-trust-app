import React from "react";
import styles from "./EvaluationModal.module.css";

const EvaluationModal = ({
  isOpen,
  onClose,
  scenario,
  details,
  onStartEvaluation,
}) => {
  if (!isOpen) return null;

  const observationDetails = details.results;

  return (
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <h2
          className={styles.header}
        >{`TRAVOS Scenario ${scenario} Results`}</h2>
        <div className={styles.modalBody}>
          <div className={styles.detailsContainer}>
            {observationDetails.map((observation, index) => {
              const observationKey = `observation(${index + 1})`;
              return (
                <div key={index} className={styles.modalBody}>
                  <p>
                    <strong>{`For Observation ${index + 1}:`}</strong>
                  </p>
                  <ul>
                    <li>Sender: {observation.sender}</li>
                    <li>Receiver: {observation.receiver}</li>
                    <li>Message: {observation[observationKey]}</li>
                    <li>Final Trust Score: {observation.final_trust_score}</li>
                    <li>
                      Final Trust Outcome: {observation.final_trust_outcome}
                    </li>
                    <li>
                      Previous Interaction History:{" "}
                      {observation.previous_history}
                    </li>
                  </ul>
                </div>
              );
            })}
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

export default EvaluationModal;
