#!/usr/bin/env bash


### Restore database from a backup.
###
### Parameters:
###     <1> filename of an existing backup.
###
### Usage:
###     $ docker-compose (exec |run --rm) db restore.sh <1>


set -o errexit
set -o pipefail
set -o nounset


working_dir="$(dirname ${0})"
source "${working_dir}/_sourced/constants.sh"
source "${working_dir}/_sourced/messages.sh"


if [[ -z ${1+x} ]]; then
    message_error "Backup filename is not specified yet it is a required parameter. Make sure you provide one and try again."
    exit 1
fi
backup_filename="/backups/${1}"
if [[ ! -f "${backup_filename}" ]]; then
    message_error "No backup with the specified filename found. Check out the 'backups' maintenance script output to see if there is one and try again."
    exit 1
fi

message_welcome "Restoring the '${DB_NAME}' database from the '${backup_filename}' backup..."

if [[ "${DB_USER}" == "postgres" ]]; then
    message_error "Restoring as 'postgres' user is not supported. Assign 'DB_USER' env with another one and try again."
    exit 1
fi

export PGHOST="${DB_SERVICE}"
export PGPORT="${DB_PORT}"
export PGUSER="${DB_USER}"
export PGPASSWORD="${DB_PASS}"
export PGDATABASE="${DB_NAME}"

message_info "Dropping the database..."
dropdb "${PGDATABASE}"

message_info "Creating a new database..."
createdb --owner="${DB_USER}"

message_info "Applying the backup to the new database..."
gunzip -c "${backup_filename}" | psql "${DB_NAME}"

message_success "The '${DB_NAME}' database has been restored from the '${backup_filename}' backup."