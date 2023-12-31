import React, { useEffect, useState } from "react";
import styles from "./Body.module.css";
import DropdownModal from "./DropdownModal";
import EvaluationModal from "./EvaluationModal";
import DetailsModal from "./DetailsModal";
import { Tooltip } from "react-tooltip";
import Dropdown from "react-bootstrap/Dropdown";
import { Button } from "react-bootstrap";
import axios from "axios";

const Body = () => {
  const [selectedScenario, setSelectedScenario] = useState(null);
  const [showDetails, setShowDetails] = useState(false);
  const [showFullDetailsModal, setShowFullDetailsModal] = useState(false);
  const [showEvaluationResults, setShowEvaluationResults] = useState(false);
  const [evaluationResults, setEvaluationResults] = useState(null);
  const [scenarioDetails, setScenarioDetails] = useState(null);

  // const baseUrl = "http://localhost:5000"; // For development
  const baseUrl = "http://51.21.101.168:5000"; //For deployment

  useEffect(() => {
    // Fetch scenario data when selectedScenario changes
    if (selectedScenario) {
      axios
        .get(`${baseUrl}/api/getScenarioDetails/${selectedScenario}`)
        .then((response) => {
          setScenarioDetails(response.data);
          setShowDetails(true);
        })
        .catch((error) => {
          console.error("Error fetching scenario details:", error);
        });
    }
  }, [selectedScenario]);

  const handleScenarioChange = (eventKey) => {
    console.log("Selected Scenario:", eventKey);

    // Toggle details visibility if the same scenario is selected again
    if (eventKey === selectedScenario) {
      setShowDetails(!showDetails);
    } else {
      // Fetch scenario data when a new scenario is selected
      axios
        .get(`${baseUrl}/api/getScenarioDetails/${eventKey}`)
        .then((response) => {
          setScenarioDetails(response.data);
          setShowDetails(true);
        })
        .catch((error) => {
          console.error("Error fetching scenario details:", error);
        });
    }

    // Update the selected scenario
    setSelectedScenario(eventKey);
  };

  const handleStartEvaluation = () => {
    // Check if a scenario is selected
    if (selectedScenario) {
      // Make a request to start evaluation for the selected scenario
      axios
        .post(`${baseUrl}/api/startEvaluation`, {
          scenario: selectedScenario,
        })
        .then((response) => {
          // Handle the response, if needed
          console.log("Evaluation started:", response.data);
          setEvaluationResults(response.data);
          setShowEvaluationResults(true);
          // You can also update the state or perform other actions based on the response
        })
        .catch((error) => {
          console.error("Error starting evaluation:", error);
        });
    } else {
      console.error("No scenario selected for evaluation");
    }
  };

  const handleCloseModal = () => {
    setShowDetails(false);
    setShowFullDetailsModal(false);
    setShowEvaluationResults(false);
  };

  const handleFullDetailsClick = (e) => {
    // Get the position of the click event
    setShowFullDetailsModal(true);
  };

  return (
    <main className={styles.main}>
      <div className={styles.textDiv}>
        <h2>
          TRAVOS: A Probabilistic Model to Evaluate Trust in the Redecentralized
          Web
        </h2>
        <div className={styles.howItWorks}>
          <p>How it Works:</p>
          <p>a) It calculates Direct Trust between two Web Applications</p>
          <p>
            b) If Direct Trust is not sufficient, then it calculates Reputation
            Trust.{" "}
            <span
              data-tip="see details"
              data-for="fullDetailsTooltip"
              className={`${styles.tooltipLink} ${styles.tooltipLinkTeal}`}
              onClick={handleFullDetailsClick}
            >
              (<strong>see More details</strong>)
            </span>
          </p>
        </div>
      </div>

      <div className={styles.dropdownDiv}>
        <p>
          Please select a Demo Scenario provided below to check the results.
        </p>
        <h2>Choose a Scenario</h2>
        <Dropdown onSelect={handleScenarioChange}>
          <Dropdown.Toggle variant="primary">
            {selectedScenario
              ? `Scenario ${selectedScenario}`
              : "Select a Scenario"}
          </Dropdown.Toggle>

          <Dropdown.Menu
            style={{
              backgroundColor: "#E8E8E8",
            }}
          >
            <Dropdown.Item eventKey="1" className={styles.dropdownItem}>
              Scenario 1
            </Dropdown.Item>
            <Dropdown.Item eventKey="2" className={styles.dropdownItem}>
              Scenario 2
            </Dropdown.Item>
            <Dropdown.Item eventKey="3" className={styles.dropdownItem}>
              Scenario 3
            </Dropdown.Item>
            <Dropdown.Item eventKey="4" className={styles.dropdownItem}>
              Scenario 4
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </div>

      <div className={styles.buttonDiv}>
        <Button
          variant="primary"
          onClick={handleStartEvaluation}
          className={styles.startButton}
        >
          Start Evaluation
        </Button>
        {/* <Button
          variant="primary"
          className={styles.reviewButton}
          onClick={handleDeleteItem}
        >
          Review Results
        </Button> */}
      </div>

      {showDetails && (
        <DropdownModal
          isOpen={showDetails}
          onClose={handleCloseModal}
          scenario={selectedScenario}
          details={scenarioDetails}
        />
      )}

      {showFullDetailsModal && (
        <DetailsModal
          isOpen={showFullDetailsModal}
          onClose={handleCloseModal}
          scenario="Full Details"
          details="Add your full details content here."
        />
      )}
      {showEvaluationResults && (
        <EvaluationModal
          isOpen={showEvaluationResults}
          onClose={handleCloseModal}
          scenario={selectedScenario}
          details={evaluationResults}
        />
      )}

      {/* React-tooltip configuration */}
      <Tooltip
        id="fullDetailsTooltip"
        place="bottom"
        effect="solid"
        className={styles.tooltipClass}
      >
        Click to see full details
      </Tooltip>
    </main>
  );
};

export default Body;
