# It often comes the situations that you want to catch a special signal/interruption/user input in your script to prevent the unpredictables.

# SIGINT: user sends an interrupt signal (Ctrl+C)
# SIGQUIT: user sends a quit signal (Ctrl+C)
# SigFPE: attempted an illegal mathematical operation
# digerlerini kill -l ile ogrenebilirsin

trap "echo Booh!" SIGINT SIGTERM
echo "It's going to run until you hit Ctrl+Z"
echo "Hit Ctrl+C to be blown away!"

while [ True ]; do
    sleep 60
done

function booh {
    echo "booh"
}
trap booh SIGINT SIGTERM
