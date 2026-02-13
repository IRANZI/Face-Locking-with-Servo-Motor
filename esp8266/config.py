# esp8266/config.py
"""
ESP8266 Configuration — MicroPython
Edit BEFORE uploading to the board.
"""

# ─── WiFi ───────────────────────────────────────────────────────────
WIFI_SSID     = "dlink_DWR-930M_26F7"       # ← CHANGE THIS
WIFI_PASSWORD = "cofounder@133"   # ← CHANGE THIS

# ─── MQTT Broker (your PC's local IP — NOT localhost) ──────────────
MQTT_BROKER   = "157.173.101.159"         
MQTT_PORT     = 1884
TEAM_ID       = "rainbows"
MQTT_TOPIC    = "vision/{}/movement".format(TEAM_ID)
CLIENT_ID     = "esp8266_{}".format(TEAM_ID)

# ─── Servo ──────────────────────────────────────────────────────────
SERVO_PIN     = 14         # GPIO14 (D5 on NodeMCU)
SERVO_MIN_ANGLE = 0        # degrees (physical limit)
SERVO_MAX_ANGLE = 180      # degrees (physical limit)
SERVO_CENTER    = 90       # neutral / centered position
SERVO_STEP      = 5        # degrees per MOVE command

# ─── PWM (50 Hz standard servo) ────────────────────────────────────
SERVO_FREQ    = 50         # Hz
# Duty range for 0-180 deg (typical SG90):
#   0°   →  duty ~  40  (0.5 ms pulse)
#   180° →  duty ~ 115  (2.5 ms pulse)
DUTY_MIN      = 40         # duty for 0°
DUTY_MAX      = 115        # duty for 180°
