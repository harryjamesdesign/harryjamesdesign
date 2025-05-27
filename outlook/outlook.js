const titles = [
      "KAI — Software Engineer",
      "Creative Technologist",
      "Frontend & 3D Specialist",
      "Senior dev and full stacker ⚡"
    ];
    let titleIndex = 0;
    let charIndex = 0;
    let deleting = false;
    const typingSpeed = 100;
    const deletingSpeed = 50;
    const delayBetween = 1500;
    const typingElement = document.getElementById("typingTitle");

    function typeLoop() {
      const current = titles[titleIndex];
      if (!deleting) {
        typingElement.textContent = current.substring(0, charIndex + 1);
        charIndex++;
        if (charIndex === current.length) {
          deleting = true;
          setTimeout(typeLoop, delayBetween);
          return;
        }
      } else {
        typingElement.textContent = current.substring(0, charIndex - 1);
        charIndex--;
        if (charIndex === 0) {
          deleting = false;
          titleIndex = (titleIndex + 1) % titles.length;
        }
      }
      setTimeout(typeLoop, deleting ? deletingSpeed : typingSpeed);
    }
    typeLoop();

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('bg'), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    const starsGeometry = new THREE.BufferGeometry();
    const starsCount = 5000;
    const starVertices = [];
    for (let i = 0; i < starsCount; i++) {
      const x = (Math.random() - 0.5) * 200;
      const y = (Math.random() - 0.5) * 200;
      const z = (Math.random() - 0.5) * 200;
      starVertices.push(x, y, z);
    }
    starsGeometry.setAttribute('position', new THREE.Float32BufferAttribute(starVertices, 3));
    const starsMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.4 });
    const starField = new THREE.Points(starsGeometry, starsMaterial);
    scene.add(starField);

    const coreGeometry = new THREE.TorusKnotGeometry(1.2, 0.4, 200, 32);
    const coreMaterial = new THREE.MeshStandardMaterial({
      color: 0x00ffff,
      metalness: 0.5,
      roughness: 0.2,
      emissive: 0x001122,
      emissiveIntensity: 0.6,
      wireframe: false,
    });
    const core = new THREE.Mesh(coreGeometry, coreMaterial);
    scene.add(core);

    const pointLight = new THREE.PointLight(0xff00ff, 1.5);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);

    const backLight = new THREE.PointLight(0x00ffff, 1);
    backLight.position.set(-5, -5, -5);
    scene.add(backLight);

    const ambientLight = new THREE.AmbientLight(0x222222);
    scene.add(ambientLight);

    function animate() {
      requestAnimationFrame(animate);
      core.rotation.x += 0.005;
      core.rotation.y += 0.01;
      starField.rotation.y += 0.0003;
      renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    