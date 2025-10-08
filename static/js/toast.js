function showToast(title, message, type = 'normal', duration = 3000, withIcon = false) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle     = document.getElementById('toast-title');
  const toastMessage   = document.getElementById('toast-message');
  const toastIcon      = document.getElementById('toast-icon');
  if (!toastComponent) return;

  toastComponent.classList.remove(
    'bg-red-50','border-red-500','text-red-700',
    'bg-green-50','border-green-500','text-green-700',
    'bg-white','border-gray-300','text-gray-800'
  );
  toastComponent.style.border = '';

  if (type === 'success') {
    toastComponent.classList.add('bg-green-50','border-green-500','text-green-700');
    toastComponent.style.border = '1px solid #22c55e';
  } else if (type === 'error') {
    toastComponent.classList.add('bg-red-50','border-red-500','text-red-700');
    toastComponent.style.border = '1px solid #ef4444';
  } else {
    toastComponent.classList.add('bg-red-50','border-red-500','text-red-700');
    toastComponent.style.border = '1px solid #ef4444';
  }

  if (toastIcon) {
    if (withIcon) {
      toastIcon.classList.remove('hidden');
      toastIcon.textContent = type === 'success' ? '✔️' : (type === 'error' ? '⛔' : '⚠️');
    } else {
      toastIcon.classList.add('hidden');
      toastIcon.textContent = '';
    }
  }

  if (toastTitle) toastTitle.textContent = title || '';
  if (toastMessage) toastMessage.textContent = message || '';

  toastComponent.classList.remove('opacity-0','-translate-y-10');
  toastComponent.classList.add('opacity-100','translate-y-0');

  clearTimeout(showToast._timer);
  showToast._timer = setTimeout(() => {
    toastComponent.classList.remove('opacity-100','translate-y-0');
    toastComponent.classList.add('opacity-0','-translate-y-10');
  }, Number(duration) || 3000);
}
