if command -v docker &> /dev/null; then
  if docker compose version &> /dev/null; then
    COMPOSE_CMD="docker-compose"
  elif docker-compose version &> /dev/null; then
    COMPOSE_CMD="docker-compose"
  else
    echo "Error: Docker Compose is not installed."
    return 1
  fi

  action() {
    local operation="$1"
    local env="$2"
    shift 2
    local args=("$@")

    if [ -z "$env" ]; then
      echo "Error: Missing argument. Usage: $operation [dev|pro]"
      return 1
    fi

    case "$env" in
      dev)
        $COMPOSE_CMD -f docker-compose-develop.yaml "$operation" "${args[@]}"
        ;;
      pro)
        $COMPOSE_CMD -f docker-compose-production.yaml "$operation" "${args[@]}"
        ;;
      setup)
        $COMPOSE_CMD -f docker-compose-setup.yaml "$operation" "${args[@]}"
        ;;
      *)
        $COMPOSE_CMD "$operation" "${args[@]}"
        ;;
    esac
  }

  build() { action "$0" "$1" "${@:2}"; }
  up()    { action "$0" "$1" "${@:2}"; }
  stop()  { action "$0" "$1" "${@:2}"; }
  down()  { action "$0" "$1" "${@:2}"; }

  # aliases for host machine, not in docker container
  alias app="docker exec -it django-app"
  alias django="app python manage.py"
  alias init="up setup && down setup && up dev -d && app python project_init.py && down dev"
fi
