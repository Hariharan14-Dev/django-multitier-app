{{/*
Expand the name of the chart.
*/}}
{{- define "worknest.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Create a fully qualified app name.
*/}}
{{- define "worknest.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- include "worknest.name" . }}
{{- end }}
{{- end }}